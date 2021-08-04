from pages.main import MainPage
import allure
from allure import step

@allure.feature('Тест на проверку Title Главной страницы')
@allure.title('Главная страница')
@allure.severity(allure.severity_level.CRITICAL)
def test_title_main_page(browser):
    catalog_page = MainPage(browser)
    with step("Открывает Главную страницу"):
        catalog_page.open_home_page()
    with step("Проверяет Title Главной страницы"):
        current_title = browser.title
        assert current_title == 'Your Store'


@allure.feature('Тест на наличие элементов Главной страницы')
@allure.title('Главная страница')
@allure.severity(allure.severity_level.CRITICAL)
def test_check_five_elements_on_main_page(browser):
    main_page = MainPage(browser)
    with step("Открывает Главную страницу"):
        main_page.open_home_page()
    with step("Проверяет элементы на Главной странице"):
        main_page.check_elements()

