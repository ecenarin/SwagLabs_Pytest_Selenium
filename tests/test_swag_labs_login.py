import pytest
from src.pageobjects.login_page import LoginPage


def test_valid_login_and_logout(make_driver):
    page = LoginPage(make_driver)
    page.go_to()
    page.login("standard_user", "secret_sauce")
    assert page.is_inventory_page_loaded()
    page.logout()


def test_invalid_login(make_driver):
    page = LoginPage(make_driver)
    page.go_to()
    page.login("standard_user", "wrong_password")
    assert "Epic sadface: Username and password do not match any user in this service" in page.get_error_message()
