# pages/base_page.py
from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.timeout = 30000  # 30 seconds
    
    # Common methods for all pages
    def navigate(self, url: str):
        self.page.goto(url)
    
    def get_title(self) -> str:
        return self.page.title()
    
    def take_screenshot(self, name: str):
        self.page.screenshot(path=f"screenshots/{name}.png")
    
    def wait_for_page_load(self):
        self.page.wait_for_load_state("networkidle")
    
    def click_element(self, selector: str):
        self.page.click(selector)
    
    def fill_text(self, selector: str, text: str):
        self.page.fill(selector, text)
    
    def get_text(self, selector: str) -> str:
        return self.page.text_content(selector) # type: ignore
    
    def is_element_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)
    
    def wait_for_element(self, selector: str):
        self.page.wait_for_selector(selector, timeout=self.timeout)