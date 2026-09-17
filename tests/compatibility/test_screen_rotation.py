import pytest
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import InvalidElementStateException
from selenium.webdriver.support.ui import WebDriverWait

from pages.products_page import ProductsPage

pytestmark = pytest.mark.compatibility


def test_products_page_should_survive_screen_rotation(
    driver: WebDriver,
) -> None:
    """验证商品列表页横竖屏切换兼容性。"""

    products_page = ProductsPage(driver)
    wait = WebDriverWait(driver, 20)

    assert products_page.is_loaded()

    try:
        try:
            driver.orientation = "LANDSCAPE"
        except InvalidElementStateException:
            assert products_page.is_loaded()

            pytest.xfail("My Demo App RN程序锁定为竖屏，当前版本不支持横屏显示。")

        wait.until(
            lambda current_driver: (
                current_driver.get_window_size()["width"]
                > current_driver.get_window_size()["height"]
            )
        )

        assert products_page.is_loaded()
        assert "Sauce Labs Backpack" in (products_page.get_visible_product_names())
    finally:
        if driver.orientation != "PORTRAIT":
            driver.orientation = "PORTRAIT"

            wait.until(
                lambda current_driver: (
                    current_driver.get_window_size()["height"]
                    > current_driver.get_window_size()["width"]
                )
            )
