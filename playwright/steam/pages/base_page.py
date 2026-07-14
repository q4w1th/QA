from playwright.sync_api import Page

class BasePage:
    """
    Base page class providing common properties and helper methods 
    shared across all Page Objects.
    """
    def __init__(self, page: Page):
        self.page = page

    def get_title(self) -> str:
        """Returns the document title of the current page."""
        return self.page.title()

    def get_url(self) -> str:
        """Returns the full URL of the current page."""
        return self.page.url
