from pages.base import Base
from locators.registration import RegistrationPageLocators
from locators.common import CommonLocators


class RegistrationPage(Base):
    path = "/index.php?route=account/register"

    def open_registration_page(self):
        self.browser.get(self.url + self.path)

    def check_elements_on_registration_page(self):
        self._find_element(RegistrationPageLocators.INPUT_NAME)
        self._find_element(RegistrationPageLocators.INPUT_LASTNAME)
        self._find_element(RegistrationPageLocators.INPUT_EMAIL)
        self._find_element(RegistrationPageLocators.INPUT_TELEPHONE)
        self._find_element(RegistrationPageLocators.INPUT_PASSWORD)
        self._find_element(RegistrationPageLocators.INPUT_PASSWORD_CONFIRM)
        self._find_element(RegistrationPageLocators.CHECKBOX_PRIVACY)
        self._find_element(RegistrationPageLocators.SUBMIT_BUTTON)

    def fill_data_in_registration_page(self):
        input_firstname = self._wait_element_to_be_clickable(RegistrationPageLocators.INPUT_NAME)
        self._input_text(input_firstname, 'Ilya')
        input_lastname = self._wait_element_to_be_clickable(RegistrationPageLocators.INPUT_LASTNAME)
        self._input_text(input_lastname, 'Ivanoff')
        input_email = self._wait_element_to_be_clickable(RegistrationPageLocators.INPUT_EMAIL)
        self._input_text(input_email, 'testuser1256@yandex.ru')
        input_telephone = self._wait_element_to_be_clickable(RegistrationPageLocators.INPUT_TELEPHONE)
        self._input_text(input_telephone, '79031231000')
        input_password = self._wait_element_to_be_clickable(RegistrationPageLocators.INPUT_PASSWORD)
        self._input_text(input_password, '1234567')
        input_password_confirm = self._wait_element_to_be_clickable(RegistrationPageLocators.INPUT_PASSWORD_CONFIRM)
        self._input_text(input_password_confirm, '1234567')
        checkbox = self._find_element(RegistrationPageLocators.CHECKBOX_PRIVACY)
        checkbox.click()
        registration_button = self._find_element(RegistrationPageLocators.SUBMIT_BUTTON)
        registration_button.click()
        # self._wait_element_to_be_presence(CommonLocators.WAIT_CONTAINER_LOAD)
