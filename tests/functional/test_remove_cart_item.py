import pytest
from appium.webdriver.webdriver import WebDriver

from pages.cart_page import CartPage
from pages.product_details_page import ProductDetailsPage
from pages.products_page import ProductsPage

pytestmark = pytest.mark.functional


def test_user_should_remove_product_from_cart(
    driver: WebDriver,
) -> None:
    """验证用户能够从购物车删除商品。"""

    products_page = ProductsPage(driver)
    product_details_page = ProductDetailsPage(driver)
    cart_page = CartPage(driver)

    assert products_page.is_loaded()

    products_page.open_backpack()
    assert product_details_page.is_loaded()

    product_details_page.add_to_cart()
    assert product_details_page.get_cart_quantity() == "1"

    product_details_page.open_cart()
    assert cart_page.is_loaded()
    assert cart_page.get_product_name() == "Sauce Labs Backpack"

    cart_page.remove_item()

    assert cart_page.wait_until_product_removed()
