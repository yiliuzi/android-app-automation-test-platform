from appium.webdriver.webdriver import WebDriver

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.product_details_page import ProductDetailsPage
from pages.products_page import ProductsPage


def test_checkout_should_navigate_to_login_page(
    driver: WebDriver,
) -> None:
    """验证未登录用户结算时会进入登录页面。"""

    products_page = ProductsPage(driver)
    product_details_page = ProductDetailsPage(driver)
    cart_page = CartPage(driver)
    login_page = LoginPage(driver)

    assert products_page.is_loaded()

    products_page.open_backpack()

    assert product_details_page.is_loaded()

    product_details_page.add_to_cart()
    product_details_page.open_cart()

    assert cart_page.is_loaded()

    cart_page.proceed_to_checkout()

    assert login_page.is_loaded()
