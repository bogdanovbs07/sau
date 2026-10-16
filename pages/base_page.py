from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page
    
    def navigate(self, url: str) -> "BasePage":
        self.page.goto(url)
        return self
    
    def click(self, selector: str) -> "BasePage":
        self.page.locator(selector).click()
        return self
    
    def fill(self, selector: str, text: str) -> "BasePage":
        self.page.locator(selector).fill(text)
        return self
    
    def expect_url(self, url_pattern: str) -> "BasePage":
        expect(self.page).to_have_url(url_pattern)
        return self
    
    def expect_text(self, selector: str, text: str) -> "BasePage":
        expect(self.page.locator(selector)).to_contain_text(text)
        return self
