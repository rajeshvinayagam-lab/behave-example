from selenium.webdriver.common.by import By


class ForgotPasswordPage:
    def __init__(self, browser):
        self.browser = browser

    def enter_email(self, email):
        self.browser.find_element(By.NAME, 'email').send_keys(email)

    def click_submit(self):
        self.browser.find_element(By.NAME, 'submit').click()

    def get_confirmation_message(self):
        return self.browser.find_element(By.ID, 'confirmation').text
