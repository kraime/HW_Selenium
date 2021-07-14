from pages.product import ProductPage
import allure
from allure import step

@allure.feature('Тест на проверку Title страницы товара')
@allure.title('Страница товара')
@allure.severity(allure.severity_level.CRITICAL)
def test_title_product_page(browser):
    catalog_page = ProductPage(browser)
    with step("Открывает страницу Товаров"):
        catalog_page.open_product_page()
    with step("Проверяет Title страницы товара"):
        current_title = browser.title
        assert current_title == 'iPhone!'


@allure.feature('Тест на наличие элементов страницы товара')
@allure.title('Страница товара')
@allure.severity(allure.severity_level.CRITICAL)
def test_product_page_elements(browser):
    product_page = ProductPage(browser)
    with step("Открывает страницу Товара"):
        product_page.open_product_page()
    with step("Проверяет элементы на странице Товара"):
        product_page.check_elements_on_product_page()

