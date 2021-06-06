from selenium.webdriver.common.by import By


class ProductPageLocators:
    ADD_TO_WISHLIST = (By.CSS_SELECTOR, ".btn.btn-default>.fa.fa-heart")
    COMPARE_PRODUCT = (By.CSS_SELECTOR, ".btn.btn-default>.fa.fa-exchange")
    ADD_TO_CART = (By.XPATH, "//button[@id='button-cart']")
    REVIEW = (By.PARTIAL_LINK_TEXT, "reviews")
    CHECK_PRODUCTS_IN_SHOPING_CART = (By.CSS_SELECTOR, "#cart-total")
