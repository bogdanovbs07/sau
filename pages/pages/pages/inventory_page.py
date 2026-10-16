from pages.base_page import BasePage

class InventoryPage(BasePage):
    BACKPACK_ADD = "#add-to-cart-sauce-labs-backpack"
    CART_LINK = ".shopping_cart_link"
    
    def add_backpack_to_cart(self) -> "InventoryPage":
        self.click(self.BACKPACK_ADD)
        return self
    
    def go_to_cart(self) -> "CartPage":
        self.click(self.CART_LINK)
        return CartPage(self.page)
