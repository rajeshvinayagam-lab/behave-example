from behave import given, when, then
from features.pages.login_page import LoginPage
from features.pages.forgot_password_page import ForgotPasswordPage
from config.config import BASE_URL, EMAIL
from config.logger import get_logger
from config.retry import retry

logger = get_logger()


# Define the steps

@given('I am on the login page')
def step_given_on_login_page(context):
    context.browser.get(f'{BASE_URL}/login.html')
    context.login_page = LoginPage(context.browser)
    context.forgot_password_page = ForgotPasswordPage(context.browser)
    logger.info("Navigated to login page")


@when('I enter {username} and {password}')
def step_when_enter_credentials(context, username, password):
    retry(lambda: context.login_page.enter_username(username))
    retry(lambda: context.login_page.enter_password(password))
    logger.info(f"Entered username: {username} and password: {password}")


@when('I click on the login button')
def step_when_click_login_button(context):
    retry(lambda: context.login_page.click_login())
    logger.info("Clicked on login button")


@then('I should see {message}')
def step_then_see_message(context, message):
    if message == "Homepage":
        assert context.browser.current_url == f'{BASE_URL}/index.html'
    elif message == "A password reset link has been sent to your email.":
        confirmation_message = context.forgot_password_page.get_confirmation_message()
        assert confirmation_message == message
    else:
        error_message = context.login_page.get_error_message()
        assert error_message == message
    logger.info(f"Expected message: {message} displayed")


@when('I click on the forgot password link')
def step_when_click_forgot_password_link(context):
    retry(lambda: context.login_page.click_forgot_password())
    logger.info("Clicked on forgot password link")


@when('I enter my email address')
def step_when_enter_email_address(context):
    retry(lambda: context.forgot_password_page.enter_email(EMAIL))
    logger.info(f"Entered email address: {EMAIL}")


@when('I click on the submit button')
def step_when_click_submit_button(context):
    retry(lambda: context.forgot_password_page.click_submit())
    logger.info("Clicked on submit button")
