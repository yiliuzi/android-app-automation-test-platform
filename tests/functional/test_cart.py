from appium.webdriver.webdriver import WebDriver

from pages.cart_page import CartPage
from pages.product_details_page import ProductDetailsPage
from pages.products_page import ProductsPage


def test_cart_should_display_added_product(
    driver: WebDriver,
) -> None:
    """验证加入购物车的商品名称、数量和价格。"""

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
    assert cart_page.get_product_price() == "$29.99"
    assert cart_page.get_item_quantity() == "1"
    assert cart_page.get_total_number() == "1 item"
    assert cart_page.get_total_price() == "$29.99"
