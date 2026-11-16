import pytest
import saucedemo.ui_configuration as ui_configuration
from saucedemo.pages.login_page import LoginPage
from saucedemo.pages.inventory_page import InventoryPage
import re
from playwright.sync_api import expect, Playwright

@pytest.fixture(scope="session", autouse=True)
def configure_test_id(playwright: Playwright):
    playwright.selectors.set_test_id_attribute("data-test")

@pytest.fixture
def cart_with_two_products(authorized_page):
    authorized_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    authorized_page.add_to_cart("Sauce Labs Backpack")
    yield authorized_page
    authorized_page.remove_button("Sauce Labs Bolt T-Shirt").click()
    authorized_page.remove_button("Sauce Labs Backpack").click()

@pytest.fixture(scope="session")
def auth_state(browser):
    # создать context, залогиниться, снять state, закрыть context, вернуть state
    context = browser.new_context()
    page = context.new_page()
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(ui_configuration.STANDARD_USER, ui_configuration.PASSWORD)
    expect(page).to_have_url(re.compile(r".*inventory"))
    state = context.storage_state()
    context.close()
    return state

@pytest.fixture
def authorized_context(browser, auth_state):
    # создать context с storage_state=auth_state, отдать через yield, закрыть после теста
    context = browser.new_context(storage_state=auth_state)
    yield context
    context.close()

@pytest.fixture
def authorized_page(authorized_context):
    # создать page в этом контексте, открыть inventory.html, вернуть InventoryPage(page)
    page = authorized_context.new_page()
    page.goto(ui_configuration.BASE_URL + "/inventory.html")
    return InventoryPage(page)