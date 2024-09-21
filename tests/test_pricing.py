import allure

from base_test import BaseTest
from util.locators import LoginPageLocators, ProductPageLocators
from configurations.config import USERNAME, PASSWORD, BASE_URL


@allure.feature("Pricing Feature")
class TestPricing(BaseTest):
    def setup_method(self):
        self.setup(headless=True)  # Set to True for headless mode or False for headed

    def teardown_method(self):
        self.teardown()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Sort products high to low")
    def test_price_order_high_to_low(self):
        self.page.goto(BASE_URL)
        self.page.fill(LoginPageLocators.USERNAME_INPUT, USERNAME)
        self.page.fill(LoginPageLocators.PASSWORD_INPUT, PASSWORD)
        self.page.click(LoginPageLocators.LOGIN_BUTTON)

        self.page.select_option(ProductPageLocators.SORT_DROPDOWN, "hilo")

        # Fetch the list of prices
        prices = self.page.locator(ProductPageLocators.PRODUCT_PRICES).all_text_contents()
        prices = [float(price.replace('$', '')) for price in prices]

        # Assert prices are in descending order
        assert prices == sorted(prices, reverse=True)
        self.take_screenshot("Sorted Items from High to low")
