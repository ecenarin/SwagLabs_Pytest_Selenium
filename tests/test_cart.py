import pytest
from selenium.webdriver.common.by import By
from src.pageobjects.login_page import LoginPage
from src.pageobjects.cart_page import CartPage
from src.locators.locators import InventoryPageLocators


def test_add_to_cart_and_verify(make_driver):
    page = LoginPage(make_driver)
    cart = CartPage(make_driver)

    # Step 1: Login
    page.go_to()
    page.login("standard_user", "secret_sauce")
    assert page.is_inventory_page_loaded()

    # Step 2: Add first product to cart
    add_buttons = make_driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")
    assert add_buttons, "No Add to cart buttons found"
    add_buttons[0].click()

    # Step 3: Verify cart badge shows 1
    assert cart.get_cart_count() == "1"

    # Step 4: Go to cart page and verify content
    cart.go_to_cart()
    assert cart.is_cart_page_loaded()
    assert cart.is_product_in_cart()
    assert cart.get_cart_item_name() != ""
    assert "$" in cart.get_cart_item_price()
