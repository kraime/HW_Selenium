from pages.main import MainPage


def test_title_main_page(browser):
    catalog_page = MainPage(browser)
    catalog_page.open_home_page()
    current_title = browser.title
    assert current_title == 'Your Store'


def test_check_five_elements_on_main_page(browser):
    main_page = MainPage(browser)
    main_page.open_home_page()
    main_page.check_elements()
