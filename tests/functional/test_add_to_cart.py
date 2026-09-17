from appium.webdriver.webdriver import WebDriver

from pages.product_details_page import ProductDetailsPage
from pages.products_page import ProductsPage


def test_user_should_add_backpack_to_cart(
    driver: WebDriver,
) -> None:
    """验证用户能够将背包商品加入购物车。"""

    products_page = ProductsPage(driver)
    product_details_page = ProductDetailsPage(driver)

    assert products_page.is_loaded()

    products_page.open_backpack()

    assert product_details_page.is_loaded()
    assert product_details_page.get_product_price() == "$29.99"

    product_details_page.add_to_cart()

    assert product_details_page.get_cart_quantity() == "1"
