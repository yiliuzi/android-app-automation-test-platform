from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class ProductsPage(BasePage):
    """商品列表页面。"""

    PRODUCTS_SCREEN = (
        AppiumBy.ACCESSIBILITY_ID,
        "products screen",
    )

    PRODUCTS_TITLE = (
        AppiumBy.XPATH,
        '//*[@text="Products"]',
    )

    PRODUCT_NAMES = (
        AppiumBy.XPATH,
        '//*[starts-with(@text, "Sauce Labs ")]',
    )

    BACKPACK_PRODUCT = (
        AppiumBy.XPATH,
        '//*[@text="Sauce Labs Backpack"]',
    )

    def is_loaded(self) -> bool:
        """判断商品列表页是否加载完成。"""
        return (
            self.find_visible(self.PRODUCTS_SCREEN).is_displayed()
            and self.find_visible(self.PRODUCTS_TITLE).is_displayed()
        )

    def get_visible_product_names(self) -> list[str]:
        """获取当前屏幕内可见的商品名称。"""
        return [
            element.text
            for element in self.find_all_visible(self.PRODUCT_NAMES)
            if element.text
        ]

    def open_backpack(self) -> None:
        """进入背包商品详情页。"""
        self.click(self.BACKPACK_PRODUCT)

    def scroll_down(self) -> None:
        """向下浏览商品列表。"""
        self.swipe_up()

    def wait_for_product(self, product_name: str) -> None:
        """等待指定商品出现在当前屏幕中。"""
        product_locator = (
            AppiumBy.XPATH,
            f'//*[@text="{product_name}"]',
        )
        self.find_visible(product_locator)
