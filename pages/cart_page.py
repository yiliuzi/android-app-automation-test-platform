from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class CartPage(BasePage):
    """购物车页面。"""

    CART_SCREEN = (
        AppiumBy.ACCESSIBILITY_ID,
        "cart screen",
    )

    CART_TITLE = (
        AppiumBy.XPATH,
        '//*[@text="My Cart"]',
    )

    PRODUCT_NAME = (
        AppiumBy.ACCESSIBILITY_ID,
        "product label",
    )

    PRODUCT_PRICE = (
        AppiumBy.ACCESSIBILITY_ID,
        "product price",
    )

    ITEM_QUANTITY = (
        AppiumBy.XPATH,
        '//*[@content-desc="counter amount"]/*[@text!=""]',
    )

    TOTAL_NUMBER = (
        AppiumBy.ACCESSIBILITY_ID,
        "total number",
    )

    TOTAL_PRICE = (
        AppiumBy.ACCESSIBILITY_ID,
        "total price",
    )

    CHECKOUT_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Proceed To Checkout button",
    )

    REMOVE_ITEM_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "remove item",
    )

    INCREASE_QUANTITY_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "counter plus button",
    )

    DECREASE_QUANTITY_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "counter minus button",
    )

    def is_loaded(self) -> bool:
        """判断购物车页面是否加载完成。"""
        return (
            self.find_visible(self.CART_SCREEN).is_displayed()
            and self.find_visible(self.CART_TITLE).is_displayed()
        )

    def get_product_name(self) -> str:
        """获取购物车中的商品名称。"""
        return self.find_visible(self.PRODUCT_NAME).text

    def get_product_price(self) -> str:
        """获取购物车中的商品价格。"""
        return self.find_visible(self.PRODUCT_PRICE).text

    def get_item_quantity(self) -> str:
        """获取购物车中的商品数量。"""
        return self.find_visible(self.ITEM_QUANTITY).text

    def get_total_number(self) -> str:
        """获取购物车商品总数。"""
        return self.find_visible(self.TOTAL_NUMBER).text

    def get_total_price(self) -> str:
        """获取购物车总价。"""
        return self.find_visible(self.TOTAL_PRICE).text

    def proceed_to_checkout(self) -> None:
        """点击结算按钮。"""
        self.click(self.CHECKOUT_BUTTON)

    def remove_item(self) -> None:
        """删除购物车中的商品。"""
        self.click(self.REMOVE_ITEM_BUTTON)

    def increase_quantity(self) -> None:
        """增加商品数量。"""
        self.click(self.INCREASE_QUANTITY_BUTTON)

    def decrease_quantity(self) -> None:
        """减少商品数量。"""
        self.click(self.DECREASE_QUANTITY_BUTTON)

    def wait_for_quantity(self, expected_quantity: int) -> None:
        """等待购物车数量更新到期望值。"""
        quantity_locator = (
            AppiumBy.XPATH,
            (f'//*[@content-desc="counter amount"]//*[@text="{expected_quantity}"]'),
        )
        self.find_visible(quantity_locator)

    def wait_until_product_removed(self) -> bool:
        """等待购物车商品被删除。"""
        return self.wait_until_not_visible(self.PRODUCT_NAME)
