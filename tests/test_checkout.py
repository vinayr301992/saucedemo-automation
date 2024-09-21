import allure

from base_test import BaseTest
from util.locators import LoginPageLocators, ProductPageLocators, CheckoutPageLocators
from configurations.config import USERNAME, PASSWORD, BASE_URL


@allure.feature("Checkout Feature")
class TestCheckout(BaseTest):
    def setup_method(self):
        self.setup(headless=True)  # Set to True for headless mode or False for headed

    def teardown_method(self):
        self.teardown()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Verify Checkout Flow")
    def test_add_items_and_checkout(self):
        self.page.goto(BASE_URL)
        self.page.fill(LoginPageLocators.USERNAME_INPUT, USERNAME)
        self.page.fill(LoginPageLocators.PASSWORD_INPUT, PASSWORD)
        self.page.click(LoginPageLocators.LOGIN_BUTTON)

        # Add items to cart
        self.page.click(ProductPageLocators.ADD_TO_CART_BACKPACK)
        self.page.click(ProductPageLocators.ADD_TO_CART_BIKE_LIGHT)
        self.page.click(ProductPageLocators.SHOPPING_CART)

        # Start checkout
        self.page.click(CheckoutPageLocators.CHECKOUT_BUTTON)
        self.page.fill(CheckoutPageLocators.FIRST_NAME_INPUT, "John")
        self.page.fill(CheckoutPageLocators.LAST_NAME_INPUT, "Doe")
        self.page.fill(CheckoutPageLocators.POSTAL_CODE_INPUT, "12345")
        self.page.click(CheckoutPageLocators.CONTINUE_BUTTON)

        # Complete purchase
        self.page.click(CheckoutPageLocators.FINISH_BUTTON)

        # Verify checkout complete
        assert self.page.locator(CheckoutPageLocators.COMPLETE_HEADER).text_content() == "Thank you for your order!"
        self.take_screenshot("Order Placement Success Page")
