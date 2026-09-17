import pytest
from appium.webdriver.webdriver import WebDriver

from pages.products_page import ProductsPage

pytestmark = pytest.mark.interruption


def test_app_should_recover_after_backgrounding(
    driver: WebDriver,
) -> None:
    """验证App进入后台后能够正常恢复。"""

    products_page = ProductsPage(driver)

    assert products_page.is_loaded()

    driver.background_app(3)

    assert products_page.is_loaded()

    product_names = products_page.get_visible_product_names()

    assert "Sauce Labs Backpack" in product_names
