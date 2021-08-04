from pages.base import Base
from locators.main import HomePageLocators


class MainPage(Base):

    def open_home_page(self):
        self.browser.get(self.url)

    def check_elements(self):
        self.logger.info('check elements')
        assert self._find_element(HomePageLocators.SEARCH)
        assert self._find_elements(HomePageLocators.CART)
        assert self._find_element(HomePageLocators.UPPER_MENU)
        assert self._find_element(HomePageLocators.CART)
        assert self._find_element(HomePageLocators.WISH_LIST)
