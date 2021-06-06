from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    INPUT_NAME = (By.ID, "input-firstname")
    INPUT_LASTNAME = (By.ID, "input-lastname")
    INPUT_EMAIL = (By.ID, "input-email")
    INPUT_TELEPHONE = (By.ID, "input-telephone")
    INPUT_PASSWORD = (By.ID, "input-password")
    INPUT_PASSWORD_CONFIRM = (By.ID, "input-confirm")
    CHECKBOX_PRIVACY = (By.NAME, "agree")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
