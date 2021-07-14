from pages.login import LoginPage
import allure
from allure import step

@allure.feature('Тест на проверку Title страницы Логина Юзера')
@allure.title('Страница Логина Юзера')
@allure.severity(allure.severity_level.CRITICAL)
def test_title_login_page(browser):
    catalog_page = LoginPage(browser)
    with step("Открывает страницу логина"):
        catalog_page.open_login_page()
    with step("Проверяет Title страницы логина"):
        current_title = browser.title
        assert current_title == 'Account Login'


@allure.feature('Тест на наличие элементов страницы Логина Юзера')
@allure.title('Страница Логина Юзера')
@allure.severity(allure.severity_level.CRITICAL)
def test_login_page_elements(browser):
    login_page = LoginPage(browser)
    with step("Открывает страницу логина"):
        login_page.open_login_page()
    with step("Проверяет элементы на странице логина"):
        login_page.check_elements_on_login_page()

