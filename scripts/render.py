"""Render README.md from data/profile.yml and README.template.md."""

from __future__ import annotations

import argparse
import sys
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined

from scripts.badges import shields_segment
from scripts.dates import (
    DateError,
    format_ym,
    humanize_months,
    humanize_years,
    months_between,
)

HEADER = "<!-- generated from README.template.md - do not edit -->\n"

CLOCK_TZ = "Asia/Karachi"


def _require_non_empty_strings(mapping: dict, *, section: str) -> None:
    """Raise ValueError naming the key path of any non-str/empty value."""
    for key, value in mapping.items():
        if not isinstance(value, str) or not value:
            raise ValueError(
                f"{section}.{key}: expected a non-empty string, got {value!r}"
            )


def build_context(profile: dict, today: date) -> dict:
    """Turn raw profile data into the values the template consumes."""
    _require_non_empty_strings(profile["identity"], section="identity")
    _require_non_empty_strings(profile["stats"], section="stats")

    career_months = months_between(
        profile["career_start"], "present", today=today, field="career_start"
    )

    roles = []
    for index, job in enumerate(profile["timeline"]):
        field = f"timeline[{index}]"
        months = months_between(job["start"], job["end"], today=today, field=field)
        roles.append(
            {
                **job,
                "start_label": format_ym(job["start"], field=f"{field}.start"),
                "end_label": format_ym(job["end"], field=f"{field}.end"),
                "tenure": humanize_months(months),
            }
        )

    return {
        "identity": profile["identity"],
        "years_experience": humanize_years(career_months),
        "stats": profile["stats"],
        "timeline": roles,
    }


def render(template_path: Path, profile: dict, today: date) -> str:
    """Render the template. Raises on any undefined or unresolved placeholder."""
    env = Environment(
        loader=FileSystemLoader(str(template_path.parent)),
        undefined=StrictUndefined,
        keep_trailing_newline=True,
        autoescape=False,
    )
    env.filters["shields"] = shields_segment

    body = env.get_template(template_path.name).render(**build_context(profile, today))
    if "{{" in body:
        raise ValueError("an unrendered placeholder remains in the output")
    return HEADER + body


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Render the profile README.")
    parser.add_argument("--data", type=Path, default=Path("data/profile.yml"))
    parser.add_argument("--template", type=Path, default=Path("README.template.md"))
    parser.add_argument("--out", type=Path, default=Path("README.md"))
    args = parser.parse_args(argv)

    profile = yaml.safe_load(args.data.read_text(encoding="utf-8"))
    today = datetime.now(ZoneInfo(CLOCK_TZ)).date()

    try:
        output = render(args.template, profile, today)
    except (DateError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    args.out.write_text(output, encoding="utf-8", newline="\n")
    print(f"wrote {args.out} for {today.isoformat()} (Asia/Karachi)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
