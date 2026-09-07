import pytest
from datetime import date

from scripts.dates import DateError, format_ym, parse_ym, humanize_months, humanize_years, months_between


def test_parse_ym_returns_year_and_month():
    assert parse_ym("2026-01", field="x") == (2026, 1)


@pytest.mark.parametrize(
    "value",
    ["2026-1", "2026-13", "2026-00", "26-01", "2026", "", "2026-01-15", "2026-01\n", "٢٠٢٦-01"],
)
def test_parse_ym_rejects_malformed_values(value):
    with pytest.raises(DateError) as exc:
        parse_ym(value, field="timeline[0].start")
    assert "timeline[0].start" in str(exc.value)


def test_parse_ym_rejects_non_strings():
    with pytest.raises(DateError):
        parse_ym(None, field="x")


def test_format_ym_renders_abbreviated_month_and_year():
    assert format_ym("2026-01", field="x") == "Jan 2026"


def test_format_ym_passes_present_through():
    assert format_ym("present", field="x") == "present"


def test_format_ym_covers_all_twelve_months():
    labels = [format_ym(f"2024-{m:02d}", field="x") for m in range(1, 13)]
    assert labels == [
        "Jan 2024", "Feb 2024", "Mar 2024", "Apr 2024",
        "May 2024", "Jun 2024", "Jul 2024", "Aug 2024",
        "Sep 2024", "Oct 2024", "Nov 2024", "Dec 2024",
    ]


TODAY = date(2026, 9, 6)


def test_months_between_two_fixed_dates():
    assert months_between("2024-08", "2026-01", today=TODAY, field="x") == 17


def test_months_between_uses_today_for_present():
    assert months_between("2023-02", "present", today=TODAY, field="x") == 43


def test_months_between_spans_year_boundaries():
    assert months_between("2023-12", "2024-01", today=TODAY, field="x") == 1


def test_months_between_rejects_inverted_range():
    with pytest.raises(DateError) as exc:
        months_between("2026-05", "2026-01", today=TODAY, field="timeline[2]")
    assert "timeline[2]" in str(exc.value)


def test_months_between_rejects_future_start():
    with pytest.raises(DateError):
        months_between("2027-01", "present", today=TODAY, field="x")


@pytest.mark.parametrize(
    "months,expected",
    [
        (43, "3.5 years"),   # 3.58 floors down, never overstates
        (41, "3 years"),     # 3.41 floors down to 3.0, not 3.5
        (42, "3.5 years"),   # exactly 3.5
        (47, "3.5 years"),   # 3.91 still floors to 3.5
        (48, "4 years"),     # exactly 4.0, ".0" stripped
        (12, "1 year"),      # singular
        (6, "0.5 years"),
        (5, "0 years"),
    ],
)
def test_humanize_years_floors_to_the_half_year(months, expected):
    assert humanize_years(months) == expected


@pytest.mark.parametrize(
    "months,expected",
    [
        (8, "8 months"),
        (1, "1 month"),
        (0, "0 months"),
        (12, "1 year"),
        (17, "1 year 5 months"),
        (24, "2 years"),
        (25, "2 years 1 month"),
    ],
)
def test_humanize_months_reads_as_prose(months, expected):
    assert humanize_months(months) == expected
