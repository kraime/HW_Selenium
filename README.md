Selenium + Python + PageObject + Allure report

1) Реализован PageObject шаблон регистрации нового юзера в магазине + тест к нему
2) Реализован PageObject шаблон открытия страницы добавления нового товара в админке
3) Все старые тесты также переписаны на PageObject паттерн

pytest --browser chrome -v 

pytest tests/test_registration_page.py -v
...
pytest tests/test_product_page.py -v

UPD: [15/07/21]

Добавлены Allure Steps к тестам, Features/Titles/Severity
Добавлена Фикстура для запуска сервера посредника, и сам тест
Добавлен скрипт clean.sh по отчиске /allure-results

allure generate -c && allure open
