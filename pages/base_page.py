from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """所有页面对象的父类。"""

    def __init__(self, driver: WebDriver, timeout: int = 20) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_visible(self, locator: tuple[str, str]) -> WebElement:
        """等待并返回可见元素。"""
        return self.wait.until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def find_all_visible(
        self,
        locator: tuple[str, str],
    ) -> list[WebElement]:
        """等待至少一个元素出现，并返回所有匹配元素。"""
        self.wait.until(expected_conditions.presence_of_element_located(locator))

        return [
            element
            for element in self.driver.find_elements(*locator)
            if element.is_displayed()
        ]

    def click(self, locator: tuple[str, str]) -> None:
        """等待元素可点击后点击。"""
        element = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        element.click()

    def swipe_up(self, percent: float = 0.75) -> None:
        """在页面主要内容区域执行向上滑动。"""

        window_size = self.driver.get_window_size()

        screen_width = window_size["width"]
        screen_height = window_size["height"]

        self.driver.execute_script(
            "mobile: swipeGesture",
            {
                "left": int(screen_width * 0.1),
                "top": int(screen_height * 0.25),
                "width": int(screen_width * 0.8),
                "height": int(screen_height * 0.6),
                "direction": "up",
                "percent": percent,
            },
        )

    def wait_until_not_visible(
        self,
        locator: tuple[str, str],
    ) -> bool:
        """等待元素从页面消失。"""
        return self.wait.until(
            expected_conditions.invisibility_of_element_located(locator)
        )
