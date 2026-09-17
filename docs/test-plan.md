# Android App 自动化与兼容性测试计划

## 1. 项目概述

本项目针对 Sauce Labs My Demo App RN 开展 Android App 自动化测试，
验证核心购物流程、异常登录、设备中断恢复以及屏幕方向兼容性。

自动化框架采用 Python、Pytest、Appium、UiAutomator2 和 Page Object
Model 实现，并使用 Allure 生成测试报告。

## 2. 测试目标

- 验证 App 能够正常安装和启动；
- 验证商品列表、商品详情和购物车功能；
- 验证商品数量和价格计算正确；
- 验证登录成功、登录失败和必填项校验；
- 验证未登录用户的结算跳转；
- 验证 App 在后台切换、锁屏和解锁后能够恢复；
- 检查 App 的横竖屏兼容性；
- 在测试失败时自动保存截图和页面源码。

## 3. 测试范围

### 3.1 功能测试

- App 启动；
- 商品列表展示；
- 商品列表滑动；
- 商品详情展示；
- 商品加入购物车；
- 购物车商品信息校验；
- 商品数量增加和减少；
- 商品总价计算；
- 删除购物车商品；
- 结算登录跳转；
- 正确账号登录；
- 锁定账号登录；
- 用户名和密码必填校验；
- 收货地址信息校验。

### 3.2 中断恢复测试

- App 切换至后台后恢复；
- 设备锁屏和解锁后恢复。

### 3.3 兼容性测试

当前执行环境：

| 项目 | 配置 |
|---|---|
| 设备 | Pixel 5 模拟器 |
| Android版本 | Android 13 |
| API Level | API 33 |
| 分辨率 | 1080 × 2340 |
| 屏幕方向 | 竖屏 |
| 自动化引擎 | UiAutomator2 |

受本机存储空间限制，暂未执行多个 Android 系统版本的兼容性矩阵。

### 3.4 不在当前范围内

- iOS 测试；
- App 性能专项测试；
- 安全渗透测试；
- 弱网工具级网络损耗测试；
- 多品牌真实设备矩阵；
- 支付系统真实扣款。

## 4. 测试策略

### 4.1 页面对象模式

页面元素和页面操作存放在 `pages` 目录，测试断言和业务场景存放在
`tests` 目录，从而降低页面元素变化对测试用例的影响。

### 4.2 显式等待

使用 Selenium `WebDriverWait` 等待页面和元素状态，不使用固定
`sleep()`，减少环境速度变化造成的不稳定失败。

### 4.3 测试隔离

每条测试通过独立 Appium 会话运行，并使用 `no_reset=False` 清理
测试状态，降低购物车和页面状态在测试之间相互影响的风险。

### 4.4 失败现场保存

测试失败时自动保存：

- 当前设备截图；
- 当前 Android 页面 XML；
- Allure 报告附件。

## 5. 测试环境

### 软件环境

- Windows
- Python 3.13
- Pytest
- Appium 3
- UiAutomator2 Driver
- Android SDK
- ADB
- Android Studio Emulator
- Allure
- Ruff

### 被测应用

- 应用名称：Sauce Labs My Demo App
- 包名：`com.saucelabs.mydemoapp.rn`
- 启动 Activity：
  `com.saucelabs.mydemoapp.rn.MainActivity`

## 6. 准入条件

开始测试前必须满足：

- Android 模拟器能够正常启动；
- `adb devices` 能识别模拟器；
- APK 已成功安装；
- Appium Server 已启动；
- UiAutomator2 Driver 已安装；
- Python 依赖已安装；
- App 能够手动启动。

## 7. 准出条件

满足以下条件后，可认为本轮测试完成：

- 核心购物流程测试通过；
- 正确登录和异常登录测试通过；
- 中断恢复测试通过；
- 已知兼容性限制得到记录；
- 不存在阻塞级缺陷；
- Allure 报告能够正常生成；
- Ruff 代码质量检查通过。

## 8. 缺陷等级

| 等级 | 说明 | 示例 |
|---|---|---|
| Blocker | 核心流程完全无法执行 | App 无法启动 |
| Critical | 核心功能失效 | 无法加入购物车或结算 |
| Major | 重要功能异常但存在替代路径 | 商品数量或价格错误 |
| Minor | 非核心功能或显示问题 | 横屏布局异常 |
| Trivial | 文案、颜色或轻微UI问题 | 提示文字不一致 |

## 9. 已知问题与限制

### 横屏兼容性限制

自动化测试尝试将设备切换为横屏时，UiAutomator2 返回：

```text
Screen rotation cannot be changed.
Is it locked programmatically?