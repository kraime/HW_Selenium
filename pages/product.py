from pages.base import Base
from locators.product import ProductPageLocators


class ProductPage(Base):
    path = "/index.php?route=product/product&product_id=40"

    def open_product_page(self):
        self.browser.get(self.url + self.path)

    def check_elements_on_product_page(self):
        self.logger.info('check elements on product page')
        assert self._find_element(ProductPageLocators.CHECK_PRODUCTS_IN_SHOPING_CART)
        assert self._find_element(ProductPageLocators.REVIEW)
        assert self._find_element(ProductPageLocators.ADD_TO_CART)
        assert self._find_element(ProductPageLocators.COMPARE_PRODUCT)
        assert self._find_element(ProductPageLocators.ADD_TO_WISHLIST)
