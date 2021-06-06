from pages.login import LoginPage


def test_title_login_page(browser):
    catalog_page = LoginPage(browser)
    catalog_page.open_login_page()
    current_title = browser.title
    assert current_title == 'Account Login'


def test_login_page_elements(browser):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    login_page.check_elements_on_login_page()
