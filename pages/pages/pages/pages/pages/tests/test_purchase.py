from pages.login_page import LoginPage

def test_purchase_flow(page):
    LoginPage(page).login("standard_user", "secret_sauce") \
        .add_backpack_to_cart() \
        .go_to_cart() \
        .proceed_to_checkout() \
        .fill_shipping_info("John", "Doe", "12345") \
        .finish_order() \
        .verify_order_complete()
