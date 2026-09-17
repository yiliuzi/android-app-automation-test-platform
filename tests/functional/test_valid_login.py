from appium.webdriver.webdriver import WebDriver

from pages.cart_page import CartPage
from pages.checkout_address_page import CheckoutAddressPage
from pages.login_page import LoginPage
from pages.product_details_page import ProductDetailsPage
from pages.products_page import ProductsPage


def test_valid_user_should_open_checkout_address_page(
    driver: WebDriver,
) -> None:
    """验证正确账号登录后能够进入收货地址页面。"""

    products_page = ProductsPage(driver)
    product_details_page = ProductDetailsPage(driver)
    cart_page = CartPage(driver)
    login_page = LoginPage(driver)
    checkout_address_page = CheckoutAddressPage(driver)

    assert products_page.is_loaded()

    products_page.open_backpack()
    assert product_details_page.is_loaded()

    product_details_page.add_to_cart()
    product_details_page.open_cart()
    assert cart_page.is_loaded()

    cart_page.proceed_to_checkout()
    assert login_page.is_loaded()

    login_page.login(
        username="bob@example.com",
        password="10203040",
    )

    assert checkout_address_page.is_loaded()
    assert checkout_address_page.get_full_name() == "Rebecca Winter"
    assert checkout_address_page.get_address_line_one() == "Mandorley 112"
    assert checkout_address_page.get_city() == "Truro"
    assert checkout_address_page.get_zip_code() == "89750"
    assert checkout_address_page.get_country() == "United Kingdom"
