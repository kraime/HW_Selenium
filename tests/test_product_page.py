from pages.product import ProductPage


def test_title_product_page(browser):
    catalog_page = ProductPage(browser)
    catalog_page.open_product_page()
    current_title = browser.title
    assert current_title == 'iPhone!'


def test_product_page_elements(browser):
    product_page = ProductPage(browser)
    product_page.open_product_page()
    product_page.check_elements_on_product_page()
