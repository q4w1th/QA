import pytest

def test_search_elden_ring(home_page, search_results_page):
    """Verifies that searching for a game displays it as the first search result."""
    home_page.navigate()
    home_page.search_for("Elden Ring")
    
    assert "Steam Search" in search_results_page.get_title()
    assert "ELDEN RING" in search_results_page.get_first_result_title()

@pytest.mark.parametrize("ageday, agemonth, ageyear, should_pass", [
    ("1",     "January", "1990", True),
    ("12",    "December", "2005", True),
    ("10",    "October", "2010", False),
])
def test_elden_ring_age_verification(age_check_page, ageday, agemonth, ageyear, should_pass):
    """Verifies that age verification gate blocks or allows access to M-rated game page."""
    elden_ring_appid = 1245620
    age_check_page.navigate(elden_ring_appid)
    age_check_page.verify_age(ageday, agemonth, ageyear)

    if should_pass:
        assert "ELDEN RING" in age_check_page.get_title()
    else:
        assert "agecheck" in age_check_page.get_url()