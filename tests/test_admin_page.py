from pages.admin import AdminPage
import time
import allure
from allure import step

@allure.feature('Добавление нового товара в админке')
@allure.title('Авторизация в Админке и Добавление нового товара')
@allure.severity(allure.severity_level.CRITICAL)
def test_create_new_order(browser, config):
    admin_page = AdminPage(browser)
    with step("Открывает страницу авторизации Admin_page"):
        admin_page.open_admin_page()
    with step("Производится авторизация на странице Admin_page"):
        admin_page.login_to_admin_page(username=config['admin-auth']['username'],
                                       password=config['admin-auth']['password'])
    with step("Проходимся по менюшке каталога и делаем клик Products"):
        admin_page.go_to_catalog_products()
        time.sleep(3)
        admin_page.check_products_page()
    with step("Попадает на форму добавления нового товара"):
        admin_page.add_new_order()

