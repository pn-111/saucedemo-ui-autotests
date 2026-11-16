import ui_configuration

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.button_login = page.get_by_role("button", name="Login")

    def open(self):
        self.page.goto(ui_configuration.BASE_URL)


    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.button_login.click()
