import os
import pytest
import logging
import configparser
from pathlib import Path
import allure
import urllib.parse
import time
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from browsermobproxy import Server, Client

from utils.allure_helper import AllureCatchLogs

DRIVERS = os.path.expanduser("~/Drivers")

logging.basicConfig(level=logging.INFO, filename="../logs/logs.log")

class MyListener(AbstractEventListener):

    def on_exception(self, exception, driver):
        logging.error(f'there is a {exception}')
        driver.save_screenshot(f'../logs/{exception}.png')


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera"], default="chrome")
    parser.addoption("--executor", action="store", default="192.168.1.247")


@pytest.fixture(scope='session')
def config():
    config = configparser.ConfigParser()
    config.read(Path(__file__).parent / 'config.ini')
    return config


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_setup():
    """Pytest setup before each test."""
    with AllureCatchLogs():
        yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call():
    """Allure hook."""
    with AllureCatchLogs():
        yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_teardown():
    """Pytest teardown after each test."""
    with AllureCatchLogs():
        yield


# Фикстура для запуска сервера посредника
@pytest.fixture
def remote(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    wd = webdriver.Remote(
        command_executor=f"http://{executor}:4444/wd/hub",
        desired_capabilities={"browserName": browser},
    )
    wd.maximize_window()
    request.addfinalizer(wd.quit)
    return wd

# Фикстура для запуска браузеров локально
@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    driver = None

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.headless = headless

        driver = webdriver.Chrome(
            options=options,
            executable_path=f"{DRIVERS}/chromedriver"
        )
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.headless = headless

        driver = webdriver.Firefox(
            options=options,
            executable_path=f"{DRIVERS}/geckodriver"
        )
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=f"{DRIVERS}/operadriver")
    else:
        raise ValueError("Driver not supported: {}".format(browser))

    driver = EventFiringWebDriver(driver, MyListener())

    request.addfinalizer(driver.quit)

    if maximized:
        driver.maximize_window()
    logger = logging.getLogger('BrowserLogger')
    logger.info('Browser {} started'.format(browser))


    return driver
