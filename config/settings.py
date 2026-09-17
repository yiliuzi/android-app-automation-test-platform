import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent

load_dotenv(PROJECT_ROOT / ".env")

APPIUM_SERVER_URL = os.getenv(
    "APPIUM_SERVER_URL",
    "http://127.0.0.1:4723",
)

PLATFORM_NAME = os.getenv(
    "PLATFORM_NAME",
    "Android",
)

AUTOMATION_NAME = os.getenv(
    "AUTOMATION_NAME",
    "UiAutomator2",
)

DEVICE_NAME = os.getenv(
    "DEVICE_NAME",
    "Pixel_5_API_33",
)

DEVICE_UDID = os.getenv(
    "DEVICE_UDID",
    "emulator-5554",
)

APP_PATH = PROJECT_ROOT / "apps" / "MyDemoApp.apk"

APP_PACKAGE = os.getenv(
    "APP_PACKAGE",
    "com.saucelabs.mydemoapp.rn",
)

APP_ACTIVITY = os.getenv(
    "APP_ACTIVITY",
    "com.saucelabs.mydemoapp.rn.MainActivity",
)
