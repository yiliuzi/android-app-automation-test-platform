import pytest
from appium.webdriver.webdriver import WebDriver

from pages.cart_page import CartPage
from pages.product_details_page import ProductDetailsPage
from pages.products_page import ProductsPage

pytestmark = pytest.mark.functional


def test_cart_should_update_quantity_and_total_price(
    driver: WebDriver,
) -> None:
    """验证增加商品数量后总数和总价能够正确更新。"""

    products_page = ProductsPage(driver)
    product_details_page = ProductDetailsPage(driver)
    cart_page = CartPage(driver)

    assert products_page.is_loaded()

    products_page.open_backpack()
    assert product_details_page.is_loaded()

    product_details_page.add_to_cart()
    product_details_page.open_cart()
    assert cart_page.is_loaded()

    assert cart_page.get_item_quantity() == "1"
    assert cart_page.get_total_number() == "1 item"
    assert cart_page.get_total_price() == "$29.99"

    cart_page.increase_quantity()
    cart_page.wait_for_quantity(2)

    assert cart_page.get_item_quantity() == "2"
    assert cart_page.get_total_number() == "2 items"
    assert cart_page.get_total_price() == "$59.98"
