from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class ProductDetailsPage(BasePage):
    """商品详情页面。"""

    PRODUCT_SCREEN = (
        AppiumBy.ACCESSIBILITY_ID,
        "product screen",
    )

    PRODUCT_NAME = (
        AppiumBy.XPATH,
        '//*[@text="Sauce Labs Backpack"]',
    )

    PRODUCT_PRICE = (
        AppiumBy.ACCESSIBILITY_ID,
        "product price",
    )

    ADD_TO_CART_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Add To Cart button",
    )

    CART_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "cart badge",
    )

    CART_QUANTITY_ONE = (
        AppiumBy.XPATH,
        '//*[@content-desc="cart badge"]//*[@text="1"]',
    )

    def is_loaded(self) -> bool:
        """判断商品详情页是否加载完成。"""
        return (
            self.find_visible(self.PRODUCT_SCREEN).is_displayed()
            and self.find_visible(self.PRODUCT_NAME).is_displayed()
        )

    def get_product_price(self) -> str:
        """获取商品价格。"""
        return self.find_visible(self.PRODUCT_PRICE).text

    def add_to_cart(self) -> None:
        """将商品加入购物车。"""
        self.click(self.ADD_TO_CART_BUTTON)

    def get_cart_quantity(self) -> str:
        """获取购物车中的商品数量。"""
        return self.find_visible(self.CART_QUANTITY_ONE).text

    def open_cart(self) -> None:
        """进入购物车页面。"""
        self.click(self.CART_BUTTON)
