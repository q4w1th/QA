from playwright.sync_api import Page
from pages.base_page import BasePage

class AgeCheckPage(BasePage):
    """
    Page Object representing the Steam store age verification gate page.
    """
    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self.day_select = page.locator("#ageDay")
        self.month_select = page.locator("#ageMonth")
        self.year_select = page.locator("#ageYear")
        self.view_product_button = page.locator("#view_product_page_btn")

    def navigate(self, app_id: int):
        """Navigates directly to the age check URL for the given App ID."""
        self.page.goto(f"https://store.steampowered.com/agecheck/app/{app_id}/")

    def verify_age(self, day: str, month: str, year: str):
        """Fills out the age verification dropdowns and clicks submit."""
        self.day_select.select_option(day)
        self.month_select.select_option(month)
        self.year_select.select_option(year)
        self.view_product_button.click()
        self.page.wait_for_load_state("load")
