import logging

from selenium.webdriver.support.select import Select

from pageobjects.base_page import BasePage
from locators.login_page import LoginPage
from utilities.wait_utils import WaitUtils

logger = logging.getLogger(__name__)

class LoginPageActions(BasePage):
    def send_email(self, email):
        element = WaitUtils.wait_for_element(self.driver, LoginPage.email_locator)
        element.clear()
        element.send_keys(email)

    def skip_email(self):
        element = WaitUtils.wait_for_element(self.driver, LoginPage.email_locator)
        element.clear()

    def send_password(self, password):
        element = WaitUtils.wait_for_element(self.driver, LoginPage.password_locator)
        element.clear()
        element.send_keys(password)

    def skip_password(self):
        element = WaitUtils.wait_for_element(self.driver, LoginPage.password_locator)
        element.clear()

    def login_user(self):
        element = WaitUtils.wait_for_element(self.driver, LoginPage.login_button_locator)
        element.click()

    def check_login_error(self):
        try:
            error_section = WaitUtils.wait_for_element(self.driver, LoginPage.login_error_locator, timeout=5)
            if error_section:
                error_text = error_section.text
                logger.info(f"Login error: {error_text}")
                print(f"Login error: {error_text}")
                return True, error_text
            else:
                return False, None
        except Exception as e:
            logger.info(f"No login errors: {e}")
            return False, None
