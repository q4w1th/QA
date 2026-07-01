from playwright.sync_api import sync_playwright

def test_steam_main_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://store.steampowered.com")
        
        assert "Steam" in page.title()
        
        browser.close()