from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class CheckoutAddressPage(BasePage):
    """结算收货地址页面。"""

    CHECKOUT_ADDRESS_SCREEN = (
        AppiumBy.ACCESSIBILITY_ID,
        "checkout address screen",
    )

    CHECKOUT_TITLE = (
        AppiumBy.XPATH,
        '//*[@text="Checkout"]',
    )

    FULL_NAME_INPUT = (
        AppiumBy.ACCESSIBILITY_ID,
        "Full Name* input field",
    )

    ADDRESS_LINE_ONE_INPUT = (
        AppiumBy.ACCESSIBILITY_ID,
        "Address Line 1* input field",
    )

    CITY_INPUT = (
        AppiumBy.ACCESSIBILITY_ID,
        "City* input field",
    )

    ZIP_CODE_INPUT = (
        AppiumBy.ACCESSIBILITY_ID,
        "Zip Code* input field",
    )

    COUNTRY_INPUT = (
        AppiumBy.ACCESSIBILITY_ID,
        "Country* input field",
    )

    TO_PAYMENT_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "To Payment button",
    )

    def is_loaded(self) -> bool:
        """判断收货地址页面是否加载完成。"""
        return (
            self.find_visible(self.CHECKOUT_ADDRESS_SCREEN).is_displayed()
            and self.find_visible(self.CHECKOUT_TITLE).is_displayed()
        )

    def get_full_name(self) -> str:
        """获取收件人姓名。"""
        return self.find_visible(self.FULL_NAME_INPUT).text

    def get_address_line_one(self) -> str:
        """获取第一行地址。"""
        return self.find_visible(self.ADDRESS_LINE_ONE_INPUT).text

    def get_city(self) -> str:
        """获取城市。"""
        return self.find_visible(self.CITY_INPUT).text

    def get_zip_code(self) -> str:
        """获取邮政编码。"""
        return self.find_visible(self.ZIP_CODE_INPUT).text

    def get_country(self) -> str:
        """获取国家。"""
        return self.find_visible(self.COUNTRY_INPUT).text

    def continue_to_payment(self) -> None:
        """进入付款信息页面。"""
        self.click(self.TO_PAYMENT_BUTTON)
