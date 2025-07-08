from src.pageobjects.base_page import BasePage
from src.locators.locators import LoginPageLocators

class LoginPage(BasePage):
    def go_to(self):
        self.navigate_to("https://www.saucedemo.com/")

    def login(self, username, password):
        self.set(LoginPageLocators.USERNAME, username)
        self.set(LoginPageLocators.PASSWORD, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def is_inventory_page_loaded(self):
        return self.get_current_url().endswith("/inventory.html")

    def logout(self):
        self.click(LoginPageLocators.BURGER_MENU)
        self.click(LoginPageLocators.LOGOUT_LINK)

    def get_error_message(self):
        return self.get_text(LoginPageLocators.ERROR_MESSAGE)
