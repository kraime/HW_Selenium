Домашняя работа по Selenium + Python + PageObject

1) Реализован PageObject шаблон регистрации нового юзера в магазине + тест к нему
2) Реализован PageObject шаблон открытия страницы добавления нового товара в админке
3) Все старые тесты также переписаны на PageObject паттерн

pytest --browser chrome -v 

pytest tests/test_registration_page.py -v
pytest tests/test_admin_page.py -v
pytest tests/test_catalog.py -v
pytest tests/test_login_page.py -v
pytest tests/test_main_page.py -v
pytest tests/test_product_page.py -v

