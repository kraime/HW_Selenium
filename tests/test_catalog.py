from pages.catalog import CatalogPage


def test_title_catalog_page(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog_page()
    current_title = browser.title
    assert current_title == 'Desktops'


def test_catalog_page_elements(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog_page()
    catalog_page.check_elements_on_catalog_page()
