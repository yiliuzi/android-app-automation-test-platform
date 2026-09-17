import pytest
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

from pages.products_page import ProductsPage

pytestmark = pytest.mark.interruption


def test_app_should_recover_after_screen_unlock(
    driver: WebDriver,
) -> None:
    """验证设备锁屏并解锁后App能够正常恢复。"""

    products_page = ProductsPage(driver)
    wait = WebDriverWait(driver, 20)

    assert products_page.is_loaded()

    try:
        driver.lock()

        wait.until(lambda current_driver: current_driver.is_locked())

        assert driver.is_locked()
    finally:
        if driver.is_locked():
            driver.unlock()

    wait.until(lambda current_driver: not current_driver.is_locked())

    assert products_page.is_loaded()

    product_names = products_page.get_visible_product_names()

    assert "Sauce Labs Backpack" in product_names
