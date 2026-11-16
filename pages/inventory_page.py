class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.button_burger_menu = page.get_by_role("button", name="Open Menu")
        self.button_logout = page.get_by_test_id("logout-sidebar-link")

    def open_menu(self):
        self.button_burger_menu.click()

    def logout(self):
        self.button_logout.click()

    def add_to_cart(self, product_name):
        card = self.page.get_by_test_id("inventory-item").filter(has_text=product_name)
        card.get_by_role("button", name="Add to cart").click()

    def cart_badge(self):
        return self.page.get_by_test_id("shopping-cart-badge")

    def remove_button(self, product_name):
        card = self.page.get_by_test_id("inventory-item").filter(has_text=product_name)
        return card.get_by_role("button", name="Remove")

    def product_card(self, product_name):
        return self.page.get_by_test_id("inventory-item").filter(has_text=product_name)