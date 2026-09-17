from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

from config.settings import APP_PACKAGE


def test_app_should_launch_successfully(driver: WebDriver) -> None:
    """验证 App 能够启动并显示商品列表页。"""

    wait = WebDriverWait(driver, 20)

    wait.until(lambda current_driver: current_driver.current_package == APP_PACKAGE)

    products_screen = wait.until(
        lambda current_driver: current_driver.find_element(
            AppiumBy.ACCESSIBILITY_ID,
            "products screen",
        )
    )

    assert driver.current_package == APP_PACKAGE
    assert products_screen.is_displayed()
