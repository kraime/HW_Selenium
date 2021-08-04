from pages.catalog import CatalogPage
import allure
from allure import step

@allure.feature('Тест на проверку Title страницы Каталога')
@allure.title('Каталог товаров')
@allure.severity(allure.severity_level.CRITICAL)
def test_title_catalog_page(browser):
    catalog_page = CatalogPage(browser)
    with step("Открывает страницу каталога"):
        catalog_page.open_catalog_page()
    with step("Проверяет Title страницы каталога"):
        current_title = browser.title
        assert current_title == 'Desktops!'


@allure.feature('Тест на наличие элементов страницы Каталога')
@allure.title('Каталог товаров')
@allure.severity(allure.severity_level.CRITICAL)
def test_catalog_page_elements(browser):
    catalog_page = CatalogPage(browser)
    with step("Открывает страницу каталога и сравнивает Title страницы"):
        catalog_page.open_catalog_page()
    with step("Проверяет элементы на странице Каталога"):
        catalog_page.check_elements_on_catalog_page()

