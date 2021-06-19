import pytest
from pages.RegistrationPage import RegistrationPage


# Данный тест позволяет открыть страницу регистрации нового юзера, проверяет все эелементы при регистрации,
# вводит тестовые данные, происходит регистрирация, и после регистрации производится проверка Заголовка страницы
def test_registration_user(browser):
    registarion_page = RegistrationPage(browser)
    registarion_page.open_registration_page()
    registarion_page.check_elements_on_registration_page()
    registarion_page.fill_data_in_registration_page()
    current_title = browser.title
    assert current_title == 'Your Account Has Been Created!'
