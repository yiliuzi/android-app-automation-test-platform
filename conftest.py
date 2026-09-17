import re
from collections.abc import Generator
from datetime import UTC, datetime

import allure
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import WebDriverException

from config.settings import (
    APP_ACTIVITY,
    APP_PACKAGE,
    APPIUM_SERVER_URL,
    AUTOMATION_NAME,
    DEVICE_NAME,
    DEVICE_UDID,
    PLATFORM_NAME,
    PROJECT_ROOT,
)


def make_safe_filename(name: str) -> str:
    """将测试名称转换为可用于文件名的格式。"""
    return re.sub(r"[^a-zA-Z0-9_-]", "_", name)


def save_failure_artifacts(
    driver: WebDriver,
    test_name: str,
) -> None:
    """保存失败截图和页面源码，并附加到 Allure 报告。"""

    timestamp = datetime.now(UTC).strftime("%Y%m%d_%H%M%S")
    safe_test_name = make_safe_filename(test_name)

    screenshot_directory = PROJECT_ROOT / "screenshots"
    page_source_directory = PROJECT_ROOT / "reports" / "page_sources"

    screenshot_directory.mkdir(parents=True, exist_ok=True)
    page_source_directory.mkdir(parents=True, exist_ok=True)

    screenshot_path = screenshot_directory / f"{safe_test_name}_{timestamp}.png"
    page_source_path = page_source_directory / f"{safe_test_name}_{timestamp}.xml"

    screenshot = driver.get_screenshot_as_png()
    page_source = driver.page_source

    screenshot_path.write_bytes(screenshot)
    page_source_path.write_text(page_source, encoding="utf-8")

    allure.attach(
        screenshot,
        name="failure-screenshot",
        attachment_type=allure.attachment_type.PNG,
    )

    allure.attach(
        page_source,
        name="failure-page-source",
        attachment_type=allure.attachment_type.XML,
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
    item: pytest.Item,
    call: pytest.CallInfo[None],
) -> Generator[None]:
    """将测试执行结果保存到测试节点。"""

    outcome = yield
    report = outcome.get_result()

    setattr(item, f"report_{report.when}", report)


@pytest.fixture
def driver(
    request: pytest.FixtureRequest,
) -> Generator[WebDriver]:
    """创建并在测试结束后关闭 Appium 会话。"""

    options = UiAutomator2Options()
    options.platform_name = PLATFORM_NAME
    options.automation_name = AUTOMATION_NAME
    options.device_name = DEVICE_NAME
    options.udid = DEVICE_UDID
    options.app_package = APP_PACKAGE
    options.app_activity = APP_ACTIVITY
    options.no_reset = False
    options.auto_grant_permissions = True
    options.new_command_timeout = 120

    mobile_driver = webdriver.Remote(
        command_executor=APPIUM_SERVER_URL,
        options=options,
    )

    try:
        yield mobile_driver
    finally:
        test_report = getattr(request.node, "report_call", None)

        if test_report is not None and test_report.failed:
            try:
                save_failure_artifacts(
                    driver=mobile_driver,
                    test_name=request.node.name,
                )
            except (OSError, WebDriverException) as capture_error:
                allure.attach(
                    str(capture_error),
                    name="artifact-capture-error",
                    attachment_type=allure.attachment_type.TEXT,
                )

        mobile_driver.quit()
