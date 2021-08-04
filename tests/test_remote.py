import time


# Тесты для удаленного запуска
def test_google_0(remote):
    remote.get("https://google.ru")
    remote.find_element_by_name("q")
    assert remote.title == "Google"
    time.sleep(1)


def test_yandex_0(remote):
    remote.get("https://ya.ru")
    remote.find_element_by_id("text")
    remote.find_element_by_css_selector("a[title='Яндекс']")
    assert remote.title == "Яндекс"
    time.sleep(1)