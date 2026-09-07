from datetime import date
from pathlib import Path

import pytest
import yaml

import scripts.render
from scripts.dates import DateError
from scripts.render import HEADER, build_context, render

TODAY = date(2026, 9, 6)

PROFILE = {
    "identity": {"name": "Test Person", "title": "Engineer"},
    "career_start": "2023-02",
    "timeline": [
        {"company": "INDUS", "title": "Senior", "location": "Lahore",
         "start": "2026-01", "end": "present", "note": "A note."},
        {"company": "Omnisoft", "title": "Dev", "location": "Lahore",
         "start": "2024-08", "end": "2026-01", "note": "Another note."},
    ],
    "stats": {"palm_vein_users": "500+", "engineers_led": "5"},
}


def write_template(tmp_path: Path, body: str) -> Path:
    path = tmp_path / "README.template.md"
    path.write_text(body, encoding="utf-8")
    return path


def test_context_computes_the_years_figure():
    context = build_context(PROFILE, TODAY)
    assert context["years_experience"] == "3.5 years"


def test_context_labels_and_tenures_each_role():
    roles = build_context(PROFILE, TODAY)["timeline"]
    assert roles[0]["start_label"] == "Jan 2026"
    assert roles[0]["end_label"] == "present"
    assert roles[0]["tenure"] == "8 months"
    assert roles[1]["tenure"] == "1 year 5 months"


def test_context_preserves_original_fields():
    roles = build_context(PROFILE, TODAY)["timeline"]
    assert roles[0]["company"] == "INDUS"
    assert roles[0]["note"] == "A note."


def test_render_prepends_the_generated_header(tmp_path):
    template = write_template(tmp_path, "hello\n")
    assert render(template, PROFILE, TODAY).startswith(HEADER)


def test_render_substitutes_the_years_figure(tmp_path):
    template = write_template(tmp_path, "{{ years_experience }}\n")
    assert "3.5 years" in render(template, PROFILE, TODAY)


def test_shields_filter_is_available_in_templates(tmp_path):
    template = write_template(tmp_path, "{{ years_experience | shields }}\n")
    assert "3.5_years" in render(template, PROFILE, TODAY)


def test_one_stat_reaches_both_badge_and_prose(tmp_path):
    template = write_template(
        tmp_path,
        "badge={{ stats.palm_vein_users | shields }} prose={{ stats.palm_vein_users }}\n",
    )
    output = render(template, PROFILE, TODAY)
    assert "badge=500%2B" in output
    assert "prose=500+" in output


def test_badge_and_alt_text_derive_from_one_variable(tmp_path):
    template = write_template(
        tmp_path,
        '<img src="badge/{{ years_experience | shields }}-x" alt="{{ years_experience }} shipping"/>\n',
    )
    output = render(template, PROFILE, TODAY)
    assert "badge/3.5_years-x" in output
    assert 'alt="3.5 years shipping"' in output


def test_undefined_placeholder_is_a_hard_failure(tmp_path):
    template = write_template(tmp_path, "{{ nope }}\n")
    with pytest.raises(Exception):
        render(template, PROFILE, TODAY)


def test_render_is_idempotent(tmp_path):
    template = write_template(tmp_path, "{{ years_experience }} {{ identity.name }}\n")
    assert render(template, PROFILE, TODAY) == render(template, PROFILE, TODAY)


def test_no_placeholder_survives_into_the_output(tmp_path):
    template = write_template(tmp_path, "{{ years_experience }}\n")
    assert "{{" not in render(template, PROFILE, TODAY)


def test_bad_date_in_data_raises_with_the_field_path(tmp_path):
    broken = {**PROFILE, "timeline": [{**PROFILE["timeline"][0], "start": "nope"}]}
    template = write_template(tmp_path, "x\n")
    with pytest.raises(DateError) as exc:
        render(template, broken, TODAY)
    assert "timeline[0]" in str(exc.value)


def test_shipped_data_file_loads_and_renders(tmp_path):
    profile = yaml.safe_load(Path("data/profile.yml").read_text(encoding="utf-8"))
    template = write_template(tmp_path, "{{ years_experience }}\n")
    assert "years" in render(template, profile, TODAY)


def test_null_stat_value_raises_with_key_path():
    broken = {**PROFILE, "stats": {**PROFILE["stats"], "engineers_led": None}}
    with pytest.raises(ValueError) as exc:
        build_context(broken, TODAY)
    assert "stats.engineers_led" in str(exc.value)


def test_null_identity_value_raises_with_key_path():
    broken = {**PROFILE, "identity": {**PROFILE["identity"], "name": None}}
    with pytest.raises(ValueError) as exc:
        build_context(broken, TODAY)
    assert "identity.name" in str(exc.value)


def test_clock_timezone_is_pinned_to_karachi():
    assert scripts.render.CLOCK_TZ == "Asia/Karachi"
