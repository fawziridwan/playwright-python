from playwright.sync_api import Page, expect
from page.BasePage import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = "[data-test='username']"
    PASSWORD_INPUT = "[data-test='password']"
    LOGIN_BTN = "[data-test='login-button']"
    ERROR_MESSAGE = "[data-test='error']"
    
    def __init__(self,page: Page):
        super().__init__(page)
        self.page = page
        
    def load(self):
        self.navigate("https://www.saucedemo.com/")
        self.wait_for_page_load()

    def enter_username(self, username: str):
        self.fill_text(self.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        self.fill_text(self.PASSWORD_INPUT, password)
        
    def click_login(self):
        self.click_element(self.LOGIN_BTN)
        
    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        
    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_message_visible(self) -> bool:
        return self.is_element_visible(self.ERROR_MESSAGE)
    
    def assert_error_message_contains(self, expected_text: str):
        actual_text = self.get_error_message()
        assert expected_text in actual_text, f"Expected error message to contain '{expected_text}', but got '{actual_text}'"