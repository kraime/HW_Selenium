from pages.admin import AdminPage
import time


def test_create_new_order(browser, config):
    admin_page = AdminPage(browser)
    # Открывает страницу авторизации Admin_page
    admin_page.open_admin_page()
    # Производится авторизация на странице Admin_page
    admin_page.login_to_admin_page(username=config['admin-auth']['username'], password=config['admin-auth']['password'])
    # Проходимся по менюшке каталога и делаем клик Products
    admin_page.go_to_catalog_products()
    time.sleep(3)
    admin_page.check_products_page()
    # Попадает на форму добавления нового товара
    admin_page.add_new_order()
