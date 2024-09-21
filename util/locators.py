class LoginPageLocators:
    USERNAME_INPUT = '//input[@id="user-name"]'
    PASSWORD_INPUT = '//input[@id="password"]'
    LOGIN_BUTTON = '//input[@id="login-button"]'


class ProductPageLocators:
    SORT_DROPDOWN = '//select[@class="product_sort_container"]'
    PRODUCT_NAMES = '//div[@class="inventory_item_name"]'
    PRODUCT_PRICES = '//div[@class="inventory_item_price"]'
    ADD_TO_CART_BACKPACK = '//button[@data-test="add-to-cart-sauce-labs-backpack"]'
    ADD_TO_CART_BIKE_LIGHT = '//button[@data-test="add-to-cart-sauce-labs-bike-light"]'
    SHOPPING_CART = '//a[@class="shopping_cart_link"]'


class CheckoutPageLocators:
    CHECKOUT_BUTTON = '//button[@data-test="checkout"]'
    FIRST_NAME_INPUT = '//input[@id="first-name"]'
    LAST_NAME_INPUT = '//input[@id="last-name"]'
    POSTAL_CODE_INPUT = '//input[@id="postal-code"]'
    CONTINUE_BUTTON = '//input[@data-test="continue"]'
    FINISH_BUTTON = '//button[@data-test="finish"]'
    COMPLETE_HEADER = '//h2[@class="complete-header"]'
