from pages.base import Base
from locators.login import LoginPageLocators


class LoginPage(Base):
    path = "/index.php?route=account/login"

    def open_login_page(self):
        self.browser.get(self.url + self.path)

    def check_elements_on_login_page(self):
        self.logger.info('check elements on login page')
        self._find_element(LoginPageLocators.LOGIN_BUTTON)
        self._find_element(LoginPageLocators.FORGOTTEN_PASSWORD)
        self._find_element(LoginPageLocators.INPUT_PASS)
        self._find_element(LoginPageLocators.TRANSACTIONS)
        self._find_element(LoginPageLocators.INPUT_EMAIL)