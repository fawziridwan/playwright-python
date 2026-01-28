import pytest
from playwright.sync_api import Page, expect
from page.LoginPage import LoginPage
from page.HomePage import HomePage

class TestLogin:
    
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.login_page = LoginPage(page)
        self.home_page = HomePage(page)
        self.login_page.load()
    
    def test_successful_login(self):
        self.login_page.login("standard_user", "secret_sauce")
        # Gunakan 'expect' untuk assertion yang lebih andal dan konsisten dengan auto-waiting
        expect(self.home_page.page.locator(HomePage.APP_LOGO)).to_be_visible()
        
    def test_invalid_username(self):
        self.login_page.login("invalid_user", "secret_sauce")
        
        # Gunakan satu assertion yang kuat dengan 'expect' yang memiliki fitur auto-waiting
        expect(self.login_page.page.locator(LoginPage.ERROR_MESSAGE)).to_have_text("Epic sadface: Username and password do not match any user in this service")