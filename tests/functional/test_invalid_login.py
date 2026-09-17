from appium.webdriver.webdriver import WebDriver

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.product_details_page import ProductDetailsPage
from pages.products_page import ProductsPage


def test_locked_user_should_not_login(
    driver: WebDriver,
) -> None:
    """验证被锁定的账号无法登录。"""

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

    login_page.login(
        username="alice@example.com",
        password="10203040",
    )

    assert login_page.get_locked_out_error() == (
        "Sorry, this user has been locked out."
    )
    assert login_page.is_loaded()
