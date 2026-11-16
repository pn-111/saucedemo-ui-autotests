import re
from playwright.sync_api import expect
from saucedemo.pages.login_page import LoginPage
import saucedemo.ui_configuration as ui_configuration

product_name = "Sauce Labs Bolt T-Shirt"

# Выход из учетной записи
def test_logout_after_login(authorized_page):
    authorized_page.open_menu()
    authorized_page.logout()
    expect(authorized_page.page).to_have_url(re.compile(r"^https://www\.saucedemo\.com/?$"))

# Проверка отображения продукта после логина
def test_product_is_displayed(authorized_page):
    expect(authorized_page.product_card(product_name)).to_be_visible()

# Добавление товара в корзину
def test_add_product_to_cart(authorized_page):
    authorized_page.add_to_cart(product_name)
    expect(authorized_page.remove_button(product_name)).to_be_visible()
    
# Счетчик корзины
def test_cart_counter_increase(authorized_page):
    authorized_page.add_to_cart(product_name)
    expect(authorized_page.cart_badge()).to_have_text("1")

# Счетчик корзины (2 продукта)
def test_two_products_in_cart(cart_with_two_products):
    expect(cart_with_two_products.cart_badge()).to_have_text("2")

# Неправильный пароль
def test_login_with_wrong_password(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(ui_configuration.STANDARD_USER, "wrong_password")
    expect(page.get_by_test_id("error")).to_be_visible()

