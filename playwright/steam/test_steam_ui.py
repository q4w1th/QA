import pytest

@pytest.mark.parametrize("ageday, agemonth, ageyear, should_pass", [
    ("1",     "January", "1990", True),
    ("12",    "December", "2005", True),
    ("10",    "October", "2010", False),
])
def test_elden_ring_page(page, ageday, agemonth, ageyear, should_pass):
    page.goto("https://store.steampowered.com/agecheck/app/1245620/")

    page.locator("#ageDay").select_option(ageday)
    page.locator("#ageMonth").select_option(agemonth)
    page.locator("#ageYear").select_option(ageyear)
    page.locator("#view_product_page_btn").click()

    if should_pass:
        assert "ELDEN RING" in page.title()
    else:
        assert "agecheck" in page.url