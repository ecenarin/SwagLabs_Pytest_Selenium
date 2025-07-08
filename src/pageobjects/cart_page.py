from src.locators.locators import CartPageLocators
from src.pageobjects.base_page import BasePage


class CartPage(BasePage):
    def get_cart_count(self):
        return self.get_text(CartPageLocators.CART_BADGE)

    def go_to_cart(self):
        self.click(CartPageLocators.CART_ICON)

    def is_cart_page_loaded(self):
        return self.get_current_url().endswith("/cart.html")

    def is_product_in_cart(self):
        try:
            self.wait_for(CartPageLocators.CART_ITEM, condition="visible")
            return True
        except:
            return False

    def get_cart_item_name(self):
        return self.get_text(CartPageLocators.ITEM_NAME)

    def get_cart_item_price(self):
        return self.get_text(CartPageLocators.ITEM_PRICE)
