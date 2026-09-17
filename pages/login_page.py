from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class LoginPage(BasePage):
    """用户登录页面。"""

    LOGIN_SCREEN = (
        AppiumBy.ACCESSIBILITY_ID,
        "login screen",
    )

    LOGIN_TITLE = (
        AppiumBy.XPATH,
        '//*[@text="Login"]',
    )

    LOCKED_OUT_ERROR = (
        AppiumBy.XPATH,
        '//*[@text="Sorry, this user has been locked out."]',
    )

    USERNAME_INPUT = (
        AppiumBy.ACCESSIBILITY_ID,
        "Username input field",
    )

    USERNAME_REQUIRED_ERROR = (
        AppiumBy.XPATH,
        '//*[@text="Username is required"]',
    )

    PASSWORD_INPUT = (
        AppiumBy.ACCESSIBILITY_ID,
        "Password input field",
    )

    PASSWORD_REQUIRED_ERROR = (
        AppiumBy.XPATH,
        '//*[@text="Password is required"]',
    )

    LOGIN_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Login button",
    )

    def is_loaded(self) -> bool:
        """判断登录页面是否加载完成。"""
        return (
            self.find_visible(self.LOGIN_SCREEN).is_displayed()
            and self.find_visible(self.USERNAME_INPUT).is_displayed()
            and self.find_visible(self.PASSWORD_INPUT).is_displayed()
        )

    def enter_username(self, username: str) -> None:
        """输入用户名。"""
        username_input = self.find_visible(self.USERNAME_INPUT)
        username_input.clear()
        username_input.send_keys(username)

    def enter_password(self, password: str) -> None:
        """输入密码。"""
        password_input = self.find_visible(self.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

    def click_login(self) -> None:
        """点击登录按钮。"""
        self.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str) -> None:
        """输入用户信息并登录。"""
        self.enter_username(username)
        self.enter_password(password)
        self.driver.hide_keyboard()
        self.click_login()

    def get_locked_out_error(self) -> str:
        """获取锁定账号的登录错误提示。"""
        return self.find_visible(self.LOCKED_OUT_ERROR).text

    def submit_empty_form(self) -> None:
        """直接提交空登录表单。"""
        self.click_login()

    def get_username_required_error(self) -> str:
        """获取用户名必填提示。"""
        return self.find_visible(self.USERNAME_REQUIRED_ERROR).text

    def submit_without_password(self, username: str) -> None:
        """填写用户名后提交空密码表单。"""
        self.enter_username(username)
        self.driver.hide_keyboard()
        self.click_login()

    def get_password_required_error(self) -> str:
        """获取密码必填提示。"""
        return self.find_visible(self.PASSWORD_REQUIRED_ERROR).text
