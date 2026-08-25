#!/usr/bin/env python3
"""Render a generated portfolio dashboard from canonical Area and Project homes."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


REQUIRED_FIELDS = ("status", "pm_scope", "income_role", "next_action")
FRONTMATTER_BOUNDARY = "---"


@dataclass(frozen=True)
class Record:
    path: Path
    link: str
    name: str
    record_type: str
    domain: str
    status: str
    pm_scope: str
    income_role: str
    next_action: str
    area_id: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault-root", required=True, type=Path)
    parser.add_argument("--source-root", required=True, action="append", type=Path)
    parser.add_argument("--dashboard", required=True, type=Path)
    parser.add_argument(
        "--domain-label",
        action="append",
        default=[],
        metavar="ID=LABEL",
        help="Ordered domain ID and human-facing label mapping.",
    )
    parser.add_argument("--today", help="Override the local YYYY-MM-DD refresh date.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit nonzero when the dashboard is absent or differs from generated output.",
    )
    return parser.parse_args()


def parse_scalar(raw: str) -> str:
    value = raw.strip()
    if not value:
        return ""
    if value.startswith('"') and value.endswith('"'):
        try:
            parsed = json.loads(value)
            return str(parsed) if parsed is not None else ""
        except json.JSONDecodeError:
            return value[1:-1]
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("''", "'")
    if value in {"null", "Null", "NULL", "~"}:
        return ""
    return value


def read_frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != FRONTMATTER_BOUNDARY:
        return {}
    data: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == FRONTMATTER_BOUNDARY:
            return data
        if not line or line[0].isspace() or ":" not in line:
            continue
        key, raw = line.split(":", 1)
        data[key.strip()] = parse_scalar(raw)
    return {}


def visible_name(path: Path) -> str:
    name = path.stem[1:]
    return re.sub(r"^\d+\s*-\s*", "", name)


def humanize_domain(domain: str) -> str:
    if domain == "unclassified":
        return "Unclassified"
    words = domain.replace("-and-", "-&-").split("-")
    return " ".join("&" if word == "&" else word.capitalize() for word in words)


def resolve_under(root: Path, configured: Path) -> Path:
    candidate = configured if configured.is_absolute() else root / configured
    return candidate.resolve()


def has_symlink_between(path: Path, root: Path) -> bool:
    current = path
    while True:
        if current.is_symlink():
            return True
        if current == root or current.parent == current:
            return False
        current = current.parent


def inventory(vault_root: Path, source_roots: list[Path]) -> list[Record]:
    records: list[Record] = []
    seen_paths: set[Path] = set()
    for configured_root in source_roots:
        root = resolve_under(vault_root, configured_root)
        if not root.is_dir():
            raise ValueError(f"Source root is missing or not a directory: {root}")
        for path in root.rglob("_*.md"):
            resolved = path.resolve()
            if resolved in seen_paths or path.stem != f"_{path.parent.name}":
                continue
            seen_paths.add(resolved)
            data = read_frontmatter(path)
            record_type = data.get("type", "")
            if record_type not in {"area", "project"}:
                continue
            try:
                link = path.relative_to(vault_root).with_suffix("").as_posix()
            except ValueError as exc:
                raise ValueError(f"Canonical home is outside the vault root: {path}") from exc
            records.append(
                Record(
                    path=path,
                    link=link,
                    name=visible_name(path),
                    record_type=record_type,
                    domain=data.get("domain", "") or "unclassified",
                    status=data.get("status", ""),
                    pm_scope=data.get("pm_scope", ""),
                    income_role=data.get("income_role", ""),
                    next_action=data.get("next_action", ""),
                    area_id=data.get("area_id", ""),
                )
            )
    return records


def parse_domain_labels(values: list[str]) -> tuple[list[str], dict[str, str]]:
    order: list[str] = []
    labels: dict[str, str] = {}
    for item in values:
        domain, separator, label = item.partition("=")
        domain = domain.strip()
        label = label.strip()
        if not separator or not domain or not label:
            raise ValueError(f"Invalid --domain-label value: {item!r}")
        if domain in labels:
            raise ValueError(f"Duplicate domain label: {domain}")
        order.append(domain)
        labels[domain] = label
    return order, labels


def escape_cell(value: str) -> str:
    compact = " ".join(value.splitlines()).strip()
    return compact.replace("|", r"\|") if compact else "—"


def render_table(title: str, records: list[Record]) -> list[str]:
    if not records:
        return []
    lines = [
        f"### {title}",
        f"| {title[:-1]} | Status | PM scope | Income role | Next action |",
        "| --- | --- | --- | --- | --- |",
    ]
    for record in sorted(records, key=lambda item: item.name.casefold()):
        linked_name = f"[[{record.link}\\|{escape_cell(record.name)}]]"
        lines.append(
            "| "
            + " | ".join(
                [
                    linked_name,
                    escape_cell(record.status),
                    escape_cell(record.pm_scope),
                    escape_cell(record.income_role),
                    escape_cell(record.next_action),
                ]
            )
            + " |"
        )
    return lines


def render_dashboard(
    records: list[Record], today: str, configured_order: list[str], labels: dict[str, str]
) -> str:
    discovered = {record.domain for record in records}
    order = [domain for domain in configured_order if domain in discovered]
    order.extend(
        sorted(
            discovered.difference(order),
            key=lambda domain: labels.get(domain, humanize_domain(domain)).casefold(),
        )
    )
    lines = [
        FRONTMATTER_BOUNDARY,
        "type: pm-portfolio-dashboard",
        f'refreshed: "{today}"',
        FRONTMATTER_BOUNDARY,
        "# Portfolio Dashboard",
    ]
    for domain in order:
        domain_records = [record for record in records if record.domain == domain]
        lines.append(f"## {labels.get(domain, humanize_domain(domain))}")
        lines.extend(render_table("Areas", [r for r in domain_records if r.record_type == "area"]))
        lines.extend(
            render_table("Projects", [r for r in domain_records if r.record_type == "project"])
        )
    return "\n".join(lines) + "\n"


def validate_target(vault_root: Path, configured_dashboard: Path) -> Path:
    configured = (
        configured_dashboard
        if configured_dashboard.is_absolute()
        else vault_root / configured_dashboard
    )
    if has_symlink_between(configured.parent, vault_root):
        raise ValueError(f"Dashboard folder must not use a symlink: {configured.parent}")
    dashboard = configured.resolve()
    parent = dashboard.parent
    if not parent.is_dir():
        raise ValueError(f"Dashboard folder is missing: {parent}")
    if dashboard.exists():
        if dashboard.is_symlink() or not dashboard.is_file():
            raise ValueError(f"Dashboard target is not a regular file: {dashboard}")
        data = read_frontmatter(dashboard)
        if data.get("type") != "pm-portfolio-dashboard":
            raise ValueError(f"Refusing to replace a non-portfolio dashboard: {dashboard}")
    return dashboard


def atomic_write(path: Path, content: str) -> None:
    mode = path.stat().st_mode & 0o777 if path.exists() else 0o644
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
        os.chmod(temporary, mode)
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def main() -> int:
    args = parse_args()
    try:
        vault_root = args.vault_root.resolve()
        if not vault_root.is_dir():
            raise ValueError(f"Vault root is missing or not a directory: {vault_root}")
        dashboard = validate_target(vault_root, args.dashboard)
        domain_order, domain_labels = parse_domain_labels(args.domain_label)
        records = inventory(vault_root, args.source_root)
        if not records:
            raise ValueError("No canonical Area or Project homes were discovered.")
        today = args.today or dt.date.today().isoformat()
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", today):
            raise ValueError(f"Invalid refresh date: {today}")
        generated = render_dashboard(records, today, domain_order, domain_labels)
        current = dashboard.read_text(encoding="utf-8") if dashboard.exists() else None
        if args.check:
            if current != generated:
                print(f"Dashboard is stale: {dashboard}", file=sys.stderr)
                return 1
            print(f"Verified {len(records)} records: {dashboard}")
            return 0
        if current != generated:
            atomic_write(dashboard, generated)
            result = "Refreshed"
        else:
            result = "Unchanged"
        unclassified = sum(record.domain == "unclassified" for record in records)
        missing = sum(
            any(not getattr(record, field) for field in REQUIRED_FIELDS) for record in records
        )
        print(
            f"{result} {dashboard} with {len(records)} records "
            f"({unclassified} unclassified, {missing} with missing overview fields)."
        )
        return 0
    except (OSError, ValueError) as exc:
        print(f"refresh-dashboards: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
