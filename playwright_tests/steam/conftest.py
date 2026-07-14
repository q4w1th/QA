import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.age_check_page import AgeCheckPage

@pytest.fixture
def home_page(page):
    """Fixture providing an instance of Steam HomePage."""
    return HomePage(page)

@pytest.fixture
def search_results_page(page):
    """Fixture providing an instance of Steam SearchResultsPage."""
    return SearchResultsPage(page)

@pytest.fixture
def age_check_page(page):
    """Fixture providing an instance of Steam AgeCheckPage."""
    return AgeCheckPage(page)
