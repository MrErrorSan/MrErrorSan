"""Pure date arithmetic for the profile README. No I/O, no template concerns."""

from __future__ import annotations

import math
import re
from datetime import date

_YM = re.compile(r"^([0-9]{4})-(0[1-9]|1[0-2])\Z")

_MONTHS = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
]

PRESENT = "present"


class DateError(ValueError):
    """Raised when a date value in profile.yml cannot be used."""


def parse_ym(value: str, *, field: str) -> tuple[int, int]:
    """Parse a 'YYYY-MM' string into (year, month)."""
    if not isinstance(value, str) or not _YM.match(value):
        raise DateError(f"{field}: expected YYYY-MM, got {value!r}")
    year, month = value.split("-")
    return int(year), int(month)


def format_ym(value: str, *, field: str) -> str:
    """Render 'YYYY-MM' as 'Mon YYYY'. The literal 'present' passes through."""
    if value == PRESENT:
        return PRESENT
    year, month = parse_ym(value, field=field)
    return f"{_MONTHS[month - 1]} {year}"


def months_between(start: str, end: str, *, today: date, field: str) -> int:
    """Whole months from start to end. 'present' resolves to today."""
    start_year, start_month = parse_ym(start, field=f"{field}.start")
    if end == PRESENT:
        end_year, end_month = today.year, today.month
    else:
        end_year, end_month = parse_ym(end, field=f"{field}.end")

    months = (end_year - start_year) * 12 + (end_month - start_month)
    if months < 0:
        raise DateError(f"{field}: end {end!r} is before start {start!r}")
    return months


def humanize_years(months: int) -> str:
    """Render a month count as years, floored to the half year."""
    value = math.floor(months / 6) / 2
    unit = "year" if value == 1 else "years"
    return f"{value:g} {unit}"


def humanize_months(months: int) -> str:
    """Render a month count as prose, e.g. '1 year 5 months'."""
    years, remainder = divmod(months, 12)
    parts = []
    if years:
        parts.append(f"{years} year" + ("" if years == 1 else "s"))
    if remainder or not years:
        parts.append(f"{remainder} month" + ("" if remainder == 1 else "s"))
    return " ".join(parts)
