import allure

from base_test import BaseTest
from util.locators import LoginPageLocators, ProductPageLocators
from configurations.config import USERNAME, PASSWORD, BASE_URL


@allure.feature("Sorting Feature")
class TestSorting(BaseTest):
    def setup_method(self):
        self.setup(headless=True)  # Set to True for headless mode or False for headed

    def teardown_method(self):
        self.teardown()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Sort products Z-A")
    def test_sorting_order_z_to_a(self):
        # Log in to the application
        self.page.goto(BASE_URL)
        self.page.fill(LoginPageLocators.USERNAME_INPUT, USERNAME)
        self.page.fill(LoginPageLocators.PASSWORD_INPUT, PASSWORD)
        self.page.click(LoginPageLocators.LOGIN_BUTTON)

        # Navigate to sorting and select Z-A
        self.page.select_option(ProductPageLocators.SORT_DROPDOWN, "za")

        # Fetch the list of item names after sorting
        items = self.page.locator(ProductPageLocators.PRODUCT_NAMES).all_text_contents()

        # Assert that the list is sorted Z-A
        assert items == sorted(items, reverse=True)
        self.take_screenshot("Sorted Items from Z to A")
