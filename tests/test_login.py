import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from features.pages.login_page import LoginPage
from features.pages.forgot_password_page import ForgotPasswordPage
from config.config import BASE_URL, EMAIL
from config.logger import get_logger
from config.retry import retry

logger = get_logger()

# Load scenarios from feature files
scenarios('../features/login.feature')
scenarios('../features/forgot_password.feature')


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@given('I am on the login page')
def step_given_on_login_page(browser):
    browser.get(f'{BASE_URL}/login.html')
    global login_page
    global forgot_password_page
    login_page = LoginPage(browser)
    forgot_password_page = ForgotPasswordPage(browser)
    logger.info("Navigated to login page")


@when(parsers.parse('I enter {username} and {password}'))
def step_when_enter_credentials(username, password):
    retry(lambda: login_page.enter_username(username))
    retry(lambda: login_page.enter_password(password))
    logger.info(f"Entered username: {username} and password: {password}")


@when('I click on the login button')
def step_when_click_login_button():
    retry(lambda: login_page.click_login())
    logger.info("Clicked on login button")


@then(parsers.parse('I should see {message}'))
def step_then_see_message(message):
    if message == "Homepage":
        assert login_page.browser.current_url == f'{BASE_URL}/index.html'
    elif message == "A password reset link has been sent to your email.":
        confirmation_message = forgot_password_page.get_confirmation_message()
        assert confirmation_message == message
    else:
        error_message = login_page.get_error_message()
        assert error_message == message
    logger.info(f"Expected message: {message} displayed")


@when('I click on the forgot password link')
def step_when_click_forgot_password_link():
    retry(lambda: login_page.click_forgot_password())
    logger.info("Clicked on forgot password link")


@when('I enter my email address')
def step_when_enter_email_address():
    retry(lambda: forgot_password_page.enter_email(EMAIL))
    logger.info(f"Entered email address: {EMAIL}")


@when('I click on the submit button')
def step_when_click_submit_button():
    retry(lambda: forgot_password_page.click_submit())
    logger.info("Clicked on submit button")
