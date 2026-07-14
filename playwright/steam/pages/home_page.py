from playwright.sync_api import Page
from pages.base_page import BasePage

class HomePage(BasePage):
    """
    Page Object representing the main Steam Store home page.
    """
    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self.search_input = page.locator("input[name='term']")

    def navigate(self):
        """Navigates to the Steam Store main page."""
        self.page.goto("https://store.steampowered.com")

    def search_for(self, term: str):
        """Fills the search input and submits the query."""
        self.search_input.fill(term)
        self.search_input.press("Enter")
        self.page.wait_for_load_state("networkidle")
