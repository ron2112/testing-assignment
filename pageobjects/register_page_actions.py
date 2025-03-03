import logging
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageobjects.base_page import BasePage
from locators.register_page import RegisterPage
from utilities.wait_utils import WaitUtils

logger = logging.getLogger(__name__)

class RegisterPageActions(BasePage):
    def send_first_name(self, first_name):
        element = WaitUtils.wait_for_element(self.driver, RegisterPage.first_name_locator)
        element.clear()
        element.send_keys(first_name)

    def skip_first_name(self):
        element = WaitUtils.wait_for_element(self.driver, RegisterPage.first_name_locator)
        element.clear()

    def send_last_name(self, last_name):
        element = WaitUtils.wait_for_element(self.driver, RegisterPage.last_name_locator)
        element.clear()
        element.send_keys(last_name)

    def skip_last_name(self):
        element = WaitUtils.wait_for_element(self.driver, RegisterPage.last_name_locator)
        element.clear()

    def select_date_of_birth(self, date_of_birth):
        element = WaitUtils.wait_for_clickable(self.driver, RegisterPage.date_of_birth_locator)
        element.clear()
        element.send_keys(date_of_birth)

    def send_street(self, street):
        element = WaitUtils.wait_for_element(self.driver, RegisterPage.street_locator)
        element.clear()
        element.send_keys(street)

    def send_postal_code(self, postalcode):
        element = WaitUtils.wait_for_element(self.driver, RegisterPage.postal_code_locator)
        element.clear()
        element.send_keys(postalcode)

    def send_city(self, city):
        element = WaitUtils.wait_for_element(self.driver, RegisterPage.city_locator)
        element.clear()
        element.send_keys(city)

    def send_state(self, state):
        element = WaitUtils.wait_for_element(self.driver, RegisterPage.state_locator)
        element.clear()
        element.send_keys(state)

    def select_country(self, country):
        element = WaitUtils.wait_for_element(self.driver, RegisterPage.country_locator)
        country_dropdown = Select(element)
        country_dropdown.select_by_visible_text(country)

    def send_phone(self, phone_number):
        element = WaitUtils.wait_for_element(self.driver, RegisterPage.phone_number_locator)
        element.clear()
        element.send_keys(phone_number)

    def send_email(self, email):
        element = WaitUtils.wait_for_element(self.driver, RegisterPage.email_locator)
        element.clear()
        element.send_keys(email)

    def skip_email(self):
        element = WaitUtils.wait_for_element(self.driver, RegisterPage.email_locator)
        element.clear()

    def send_wrong_email_format(self, wrong_email):
        element = WaitUtils.wait_for_element(self.driver, RegisterPage.email_locator)
        element.clear()
        element.send_keys(wrong_email)

    def send_password(self, password):
        element = WaitUtils.wait_for_element(self.driver, RegisterPage.password_locator)
        element.clear()
        element.send_keys(password)

    def skip_password(self):
        element = WaitUtils.wait_for_element(self.driver, RegisterPage.password_locator)
        element.clear()

    def register_user(self):
        element = WaitUtils.wait_for_clickable(self.driver, RegisterPage.register_button_locator)
        element.click()

    # error functions
    def check_register_error(self):
        try:
            error_section = WaitUtils.wait_for_element(self.driver, RegisterPage.register_error_locator, timeout=5)
            if error_section:
                error_text = error_section.text
                logger.info(f"Registration error: {error_text}")
                print(f"Registration error: {error_text}")
                return True, error_text
            else:
                return False, None
        except Exception as e:
            logger.info(f"No registration errors: {e}")
            return False, None

    def chck_weak_password(self):
        try:
            weak_password = WaitUtils.wait_for_element(self.driver, RegisterPage.password_detection_locator, timeout=5)
            if weak_password:
                return True
            else:
                return False
        except Exception as e:
            logger.info(f"Weak password detection failed: {e}")
            return False

    def check_skipped_field(self):
        try:
            no_first_name = WaitUtils.wait_for_element(self.driver, RegisterPage.first_name_blank_locator)
            no_last_name = WaitUtils.wait_for_element(self.driver, RegisterPage.last_name_blank_locator)
            no_email = WaitUtils.wait_for_element(self.driver, RegisterPage.email_blank_locator)
            no_password = WaitUtils.wait_for_element(self.driver, RegisterPage.password_blank_locator)
            if no_first_name or no_last_name or no_email or no_password:
                return True
            else:
                return False
        except Exception as e:
            logger.info(f"An error occurred: {e}")
            return False

    def check_valid_email(self, email):
        try:
            email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if re.fullmatch(email_regex, email):
                return True
            else:
                return False
        except Exception as e:
            logger.info(f"An error occurred: {e}")
            return False
