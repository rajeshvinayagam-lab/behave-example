from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def enter_username(self, username):
        self.browser.find_element(By.NAME, 'username').send_keys(username)

    def enter_password(self, password):
        self.browser.find_element(By.NAME, 'password').send_keys(password)

    def click_login(self):
        self.browser.find_element(By.NAME, 'login').click()

    def click_forgot_password(self):
        self.browser.find_element(By.ID, 'forgot-password').click()

    def get_error_message(self):
        return self.browser.find_element(By.ID, 'error').text
