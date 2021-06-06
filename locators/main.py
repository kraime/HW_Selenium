from selenium.webdriver.common.by import By


class HomePageLocators:
    UPPER_MENU = (By.CLASS_NAME, "navbar-header")
    SEARCH = (By.NAME, "search")
    CART = (By.CSS_SELECTOR, "#cart > .btn")
    MY_ACCOUNT = (By.CSS_SELECTOR, ".fa.fa-user")
    WISH_LIST = (By.CSS_SELECTOR, "#wishlist-total")