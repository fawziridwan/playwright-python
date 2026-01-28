from playwright.sync_api import Page, expect
from page.BasePage import BasePage

class HomePage(BasePage):
    APP_LOGO = ".app_logo"
    TITLE_PRODUCTS = ".title"
    NAVIGATION_BAR = ".bm-burger-button"
    LOGOUT_LINK = "#logout_sidebar_link"
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        
    def is_logo_visible(self) -> bool:
        return self.is_element_visible(self.APP_LOGO)
    
    def is_products_title_visible(self) -> bool:
        return self.is_element_visible(self.TITLE_PRODUCTS)
    
    def assert_logo_text_contains(self, expected_text: str):
        actual_text = self.get_text(self.APP_LOGO)
        assert expected_text in actual_text, f"Expected logo text to contain '{expected_text}', but got '{actual_text}'"