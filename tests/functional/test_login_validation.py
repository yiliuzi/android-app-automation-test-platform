from appium.webdriver.webdriver import WebDriver

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.product_details_page import ProductDetailsPage
from pages.products_page import ProductsPage


def open_login_page(driver: WebDriver) -> LoginPage:
    """从商品列表进入结算登录页面。"""

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

    return login_page


def test_empty_username_should_display_required_error(
    driver: WebDriver,
) -> None:
    """验证用户名为空时显示必填提示。"""

    login_page = open_login_page(driver)

    login_page.submit_empty_form()

    assert login_page.get_username_required_error() == ("Username is required")
    assert login_page.is_loaded()


def test_empty_password_should_display_required_error(
    driver: WebDriver,
) -> None:
    """验证密码为空时显示必填提示。"""

    login_page = open_login_page(driver)

    login_page.submit_without_password(
        username="bob@example.com",
    )

    assert login_page.get_password_required_error() == ("Password is required")
    assert login_page.is_loaded()
