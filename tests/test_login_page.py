import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait

URL_LOGIN_PAGE = "http://demo-opencart.ru/index.php?route=account/login"


# Параметризация тестовой функции для проверки Title
@pytest.mark.parametrize("url, title", [
    ("http://demo-opencart.ru/index.php?route=account/login", "Account Login")
])
def test_title_login_page(browser, url, title):
    browser.get(url)
    current_title = browser.title
    assert current_title == title, "Неверный Title на странице Login Page"


# Проверка количества элементов меню на странице каталога
def test_login_page_menu(browser):
    browser.get(URL_LOGIN_PAGE)
    wait = WebDriverWait(browser, 3)
    menu_items = browser.find_elements_by_css_selector("ul.navbar-nav > li")
    assert len(menu_items) == 8, "Неверное количество элементов меню"


# Проверка количества блоков меню справа на странице Login Page
def test_check_right_blocks_menu_login_page(browser):
    browser.get(URL_LOGIN_PAGE)
    wait = WebDriverWait(browser, 3)
    fetured_items = browser.find_elements_by_class_name("list-group-item")
    assert len(fetured_items) == 12, "Неверное количество блоков меню справа на странице Login Page"


# Проверка количества списков ссылок в футере на странице каталога
def test_login_page_footer_blocks(browser):
    browser.get(URL_LOGIN_PAGE)
    wait = WebDriverWait(browser, 3)
    footer_blocks = browser.find_elements_by_xpath("//footer//ul")
    assert len(footer_blocks) == 4, "Неверное количество списков ссылок в футере"
