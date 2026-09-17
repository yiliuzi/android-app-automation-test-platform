import pytest
from appium.webdriver.webdriver import WebDriver

from pages.products_page import ProductsPage

pytestmark = pytest.mark.functional


def test_user_should_find_product_after_swiping(
    driver: WebDriver,
) -> None:
    """验证用户滑动列表后能够看到底部商品。"""

    products_page = ProductsPage(driver)

    assert products_page.is_loaded()

    products_page.scroll_down()
    products_page.wait_for_product("Sauce Labs Onesie")

    product_names = products_page.get_visible_product_names()

    assert "Sauce Labs Onesie" in product_names
