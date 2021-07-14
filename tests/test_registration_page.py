import pytest
from pages.RegistrationPage import RegistrationPage
import allure
from allure import step

# Данный тест позволяет открыть страницу регистрации нового юзера, проверяет все эелементы при регистрации,
# вводит тестовые данные, происходит регистрирация, и после регистрации производится проверка Заголовка страницы
@allure.feature('Регистрация нового юзера в интернет магазине')
@allure.title('Страница регистрации нового юзера')
@allure.severity(allure.severity_level.CRITICAL)
def test_registration_user(browser):
    registarion_page = RegistrationPage(browser)
    with step("Открывает страницу регистрации нового юзера"):
        registarion_page.open_registration_page()
    with step("Проверяет элементы на странице регистрации"):
        registarion_page.check_elements_on_registration_page()
    with step("Заполняет данные полей для регистрации"):
        registarion_page.fill_data_in_registration_page()
    with step("Проверяет Title страницы успешной регистрации"):
        current_title = browser.title
        assert current_title == 'Your Account Has Been Created!'

