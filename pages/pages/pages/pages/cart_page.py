from pages.base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BUTTON = "#checkout"
    
    def proceed_to_checkout(self) -> "CheckoutPage":
        self.click(self.CHECKOUT_BUTTON)
        return CheckoutPage(self.page)
