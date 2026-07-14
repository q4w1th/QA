from playwright.sync_api import Page
from pages.base_page import BasePage

class SearchResultsPage(BasePage):
    """
    Page Object representing the search results page on Steam.
    """
    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self.first_result_title = page.locator(".title").first

    def get_first_result_title(self) -> str:
        """Returns the inner text of the first game in the search results list."""
        return self.first_result_title.inner_text()
