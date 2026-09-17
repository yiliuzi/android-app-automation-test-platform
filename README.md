# Android App 自动化与兼容性测试平台

基于 Python、Pytest、Appium 和 UiAutomator2 构建的 Android App
自动化测试项目。

项目以 Sauce Labs My Demo App 为测试对象，覆盖 App 启动、商品浏览、
手势滑动、购物车、登录、结算、中断恢复和屏幕方向兼容性等场景。

## 技术栈

- Python 3.13
- Pytest
- Appium 3
- Appium Python Client
- UiAutomator2
- Android SDK / ADB
- Page Object Model
- Allure Report
- Ruff
- Android Studio Emulator

## 测试环境

| 项目 | 配置 |
|---|---|
| 操作系统 | Windows |
| 模拟设备 | Pixel 5 |
| Android 版本 | Android 13 |
| API Level | API 33 |
| 分辨率 | 1080 × 2340 |
| 自动化引擎 | UiAutomator2 |
| Appium Server | 127.0.0.1:4723 |
| 被测应用 | Sauce Labs My Demo App RN 1.3.0 |

受本机存储空间限制，当前主要在 Android 13（API 33）模拟器完成验证。
框架支持通过 `.env` 切换其他模拟器或 Android 真机。

## 项目结构

```text
android-app-automation-test-platform/
├── apps/                     # 被测 APK
├── config/                   # 环境与设备配置
├── data/                     # 测试数据和页面结构文件
├── docs/                     # 测试计划、测试报告等文档
├── pages/                    # Page Object 页面对象
├── reports/                  # Allure结果和失败页面源码
├── screenshots/              # 失败截图
├── scripts/                  # 辅助脚本
├── tests/
│   ├── functional/           # 核心业务功能测试
│   ├── compatibility/        # 兼容性测试
│   └── interruption/         # 中断恢复测试
├── conftest.py               # Appium Driver和公共Fixture
├── pytest.ini                # Pytest标记配置
├── requirements.txt          # Python依赖
├── .env.example              # 环境变量示例
└── README.md
```

## 已覆盖场景

### 功能测试

- App 启动与商品列表加载
- 商品列表数据展示
- 商品列表滑动手势
- 商品详情页展示
- 商品加入购物车
- 购物车商品名称、数量和价格校验
- 购物车数量增加及总价计算
- 从购物车删除商品
- 未登录用户结算跳转
- 正确账号登录
- 锁定账号登录失败
- 用户名和密码必填校验
- 收货地址信息校验

### 中断恢复测试

- App 切换到后台后恢复
- 设备锁屏、解锁后恢复

### 兼容性测试

- Pixel 5 / Android 13 / API 33
- 横竖屏切换检查

被测 App 当前版本在程序中锁定竖屏，因此横屏场景使用
`XFAIL` 记录为已知兼容性限制。

## 环境准备

### 1. 创建虚拟环境

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. 安装 Python 依赖

```powershell
python -m pip install -r requirements.txt
```

### 3. 安装 Appium 驱动

```powershell
appium driver install uiautomator2
appium driver list --installed
```

### 4. 配置环境变量

复制配置示例：

```powershell
Copy-Item .env.example .env
```

根据实际设备修改 `.env`：

```dotenv
APPIUM_SERVER_URL=http://127.0.0.1:4723

PLATFORM_NAME=Android
AUTOMATION_NAME=UiAutomator2

DEVICE_NAME=Pixel_5_API_33
DEVICE_UDID=emulator-5554

APP_PACKAGE=com.saucelabs.mydemoapp.rn
APP_ACTIVITY=com.saucelabs.mydemoapp.rn.MainActivity
```

### 5. 启动模拟器并安装 APK

```powershell
adb devices
adb install -r .\apps\MyDemoApp.apk
```

### 6. 启动 Appium

打开一个单独的 PowerShell：

```powershell
appium
```

Appium 服务默认地址：

```text
http://127.0.0.1:4723
```

## 运行测试

### 运行全部测试

```powershell
python -m pytest -v -s
```

### 运行功能测试

```powershell
python -m pytest tests\functional -v -s
```

### 运行中断测试

```powershell
python -m pytest -m interruption -v -s
```

### 运行兼容性测试

```powershell
python -m pytest -m compatibility -v -s
```

## Allure 报告

生成测试结果：

```powershell
python -m pytest -v -s `
    --alluredir=reports\allure-results `
    --clean-alluredir
```

打开报告：

```powershell
allure serve reports\allure-results
```

## 代码质量检查

```powershell
python -m ruff check .
python -m ruff format --check .
```

自动修复和格式化：

```powershell
python -m ruff check . --fix
python -m ruff format .
```

## 失败现场保存

测试失败时，框架会自动保存：

- App 当前截图；
- Android 页面 XML 源码；
- Allure 报告附件。

保存目录：

```text
screenshots/
reports/page_sources/
reports/allure-results/
```

这些信息可以用于定位元素变化、页面跳转失败、设备状态异常和兼容性问题。

## 框架特点

- 使用 Page Object Model 分离页面定位和测试逻辑；
- 使用显式等待代替固定休眠；
- 使用 Pytest Fixture 管理 Appium 会话；
- 使用 `.env` 管理设备和运行环境；
- 自动保存失败截图和页面源码；
- 支持功能、中断与兼容性测试分类；
- 支持 Allure 可视化测试报告；
- 使用 Ruff 统一代码质量和格式。