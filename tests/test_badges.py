import pytest

from scripts.badges import shields_segment


def test_spaces_become_underscores():
    assert shields_segment("shipping production software") == "shipping_production_software"


def test_years_figure_encodes_for_a_badge_path():
    assert shields_segment("3.5 years") == "3.5_years"


def test_hyphens_are_doubled_so_they_are_not_read_as_delimiters():
    assert shields_segment("dev-saad-shafiq") == "dev--saad--shafiq"


def test_underscores_are_doubled_so_they_are_not_read_as_spaces():
    assert shields_segment("a_b") == "a__b"


def test_plus_is_percent_encoded():
    assert shields_segment("500+") == "500%2B"


def test_at_sign_in_an_email_is_percent_encoded():
    assert shields_segment("dev.saadshafiq@gmail.com") == "dev.saadshafiq%40gmail.com"


def test_underscore_adjacent_to_space_is_a_known_ambiguity():
    # Both "a _b" and "a_ b" encode to "a___b" due to shields.io's escape alphabet.
    # When shields.io decodes "a___b" greedily, it produces "a_ b", so one input
    # round-trips incorrectly. This is a documented limitation; badge text should
    # avoid underscore-space combinations.
    assert shields_segment("a _b") == "a___b"
    assert shields_segment("a_ b") == "a___b"


def test_none_raises_type_error():
    with pytest.raises(TypeError, match="shields_segment expects str"):
        shields_segment(None)


def test_int_raises_type_error():
    with pytest.raises(TypeError, match="shields_segment expects str"):
        shields_segment(500)
