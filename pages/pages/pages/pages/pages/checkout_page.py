from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POSTAL_CODE = "#postal-code"
    CONTINUE_BUTTON = "#continue"
    FINISH_BUTTON = "#finish"
    COMPLETE_HEADER = ".complete-header"
    
    def fill_shipping_info(self, first: str, last: str, zip_code: str) -> "CheckoutPage":
        self.fill(self.FIRST_NAME, first)
        self.fill(self.LAST_NAME, last)
        self.fill(self.POSTAL_CODE, zip_code)
        self.click(self.CONTINUE_BUTTON)
        return self
    
    def finish_order(self) -> "CheckoutPage":
        self.click(self.FINISH_BUTTON)
        return self
    
    def verify_order_complete(self) -> "CheckoutPage":
        self.expect_text(self.COMPLETE_HEADER, "Thank you for your order!")
        return self
