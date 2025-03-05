import pytest
import logging
import time

from Lib.test.test_copy import order_comparisons

from conftest import skip_register_details
from data.configuration import Configuration
from pageobjects.dashboard_page_actions import DashboardPageActions
from pageobjects.register_page_actions import RegisterPageActions

logger = logging.getLogger(__name__)

class TestRegister:
    @pytest.mark(order=1)
    @pytest.mark.registration
    def test_01_normal_register(self, fill_register_details):
        try:
            self.driver = fill_register_details
            rpa  = RegisterPageActions(driver=self.driver)

            logger.info("Register page")
            print("Register page")
            rpa.register_user()

            has_errors, error_message = rpa.check_register_error()
            if not has_errors:
                logger.info("Registration successful")
                print("Registration successful")

                print("Login page")
            else:
                print(f"Error registering the user: {error_message}")
                raise AssertionError(f"Please provide correct credentials to successfully run the registration testcase")
        except Exception as e:
            raise AssertionError(f"An error occurred: {e}")
        finally:
            self.driver.quit()

    @pytest.mark(order=2)
    @pytest.mark.registration
    def test_02_existing_user_registration(self, fill_register_details):
        try:
            self.driver = fill_register_details
            rpa  = RegisterPageActions(driver=self.driver)

            existing_email = Configuration.email
            rpa.send_email(existing_email)
            rpa.register_user()

            has_errors, error_message = rpa.check_register_error()
            if has_errors and error_message.lower() == "A customer with this email address already exists.".lower():
                logger.error(f"Registration unsuccessful: {error_message}")
                print(f"Registration unsuccessful: {error_message}")
            else:
                raise AssertionError("Please provide an existing email to run testcase for existing email registration")
        except Exception as e:
            raise AssertionError(f"An error occurred: {e}")
        finally:
            self.driver.quit()

    @pytest.mark(order=3)
    @pytest.mark.registration
    def test_03_weak_password_detection(self, fill_register_details):
        try:
            self.driver = fill_register_details
            rpa  = RegisterPageActions(driver=self.driver)

            rpa.send_password(Configuration.weak_password)
            rpa.register_user()

            has_weak_password = rpa.chck_weak_password()

            if has_weak_password:
                logger.error("Password must be 8 characters and contain uppercase and lowercase letters, special character and umber")
                print("Password must be 8 characters and contain uppercase and lowercase letters, special character and umber")
            else:
                raise AssertionError("Please provide an weak password to run testcase for weak password check")
        except Exception as e:
            raise AssertionError(f"An error occurred: {e}")
        finally:
            self.driver.quit()

    @pytest.mark(order=4)
    @pytest.mark.registration
    def test_04_skip_fields(self, skip_register_details):
        try:
            self.driver = skip_register_details
            rpa = RegisterPageActions(driver=self.driver)

            rpa.register_user()

            has_missing_fields = rpa.check_skipped_field()
            if has_missing_fields:
                logger.error("First name, last name, email password all fields need to be provided")
                print("First name, last name, email password all fields need to be provided")
            else:
                raise AssertionError("Skip first name, last name, email or password to run the testcase for missing required fields")
        except Exception as e:
            raise AssertionError(f"An error occurred: {e}")
        finally:
            self.driver.quit()

    @pytest.mark(order=5)
    @pytest.mark.registration
    def test_05_invalid_email(self, check_invalid_email):
        try:
            self.driver = check_invalid_email
            rpa = RegisterPageActions(driver=self.driver)

            rpa.register_user()

            is_valid_email = rpa.check_valid_email(Configuration.invalid_email)

            if not is_valid_email:
                logger.error("Please provide a valid email")
                print("Please provide a valid email")
            else:
                raise AssertionError("Provide an invalid email address to run the testcase for checking invalid email handling")
        except Exception as e:
            raise AssertionError(f"An error occurred: {e}")
        finally:
            self.driver.quit()