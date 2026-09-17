from appium.webdriver.webdriver import WebDriver

from pages.products_page import ProductsPage


def test_products_page_should_display_product_list(
    driver: WebDriver,
) -> None:
    """验证商品列表页能够显示商品信息。"""

    products_page = ProductsPage(driver)

    assert products_page.is_loaded()

    product_names = products_page.get_visible_product_names()

    assert product_names
    assert "Sauce Labs Backpack" in product_names
    assert "Sauce Labs Bike Light" in product_names
