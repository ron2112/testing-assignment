import time

import pytest

from conftest import fill_login_details
from data.configuration import Configuration
from pageobjects.login_page_actions import LoginPageActions
from pageobjects.register_page_actions import RegisterPageActions
import logging

logger = logging.getLogger(__name__)

class TestLogin:
    @pytest.mark.run(order=1)
    @pytest.mark.login
    def test_01_successful_register(self, fill_register_details):
        try:
            self.driver = fill_register_details
            rpa = RegisterPageActions(driver=self.driver)

            logger.info("Register page open")
            print("Register page open")
            rpa.register_user()

            has_errors, error_message = rpa.check_register_error()
            if not has_errors:
                logger.info("Registration successful")
                print("Registration successful")

                print("Open login page")
            else:
                print(f"Register failed due to error :- {error_message}")
                raise AssertionError("Please provide correct credentials to successfully run the registration testcase")
        except Exception as e:
            raise AssertionError(f"An error occurred: {e}")
        finally:
            self.driver.quit()

    @pytest.mark.run(order=2)
    @pytest.mark.login
    def test_02_successful_login(self, fill_login_details):
        try:
            self.driver = fill_login_details
            signin = LoginPageActions(driver=self.driver)
            signin.login_user()

            # check there are any errors present or not
            has_errors, error_message = signin.check_login_error()
            if not has_errors:
                logger.info("Login successful!!")
                print("Login successful!!")
            else:
                print(f"Login failed due to errors :- {error_message}")
                raise AssertionError(f"Please provide all correct details to run testcase :- Successful Login")

        except Exception as err:
            raise AssertionError(f"Error occurred: {err}")
        finally:
            self.driver.quit()

    @pytest.mark.run(order=3)
    @pytest.mark.login
    def test_03_invalid_login(self, login_invalid_credentials):
        try:
            self.driver = login_invalid_credentials
            signin = LoginPageActions(self.driver)
            signin.login_user()

            # check there are any errors present or not
            has_errors, error_message = signin.check_login_error()
            if has_errors:
                logger.info("Invalid email or password")
                print("Invalid email or password")
            else:
                print(f"Login successful")
                raise AssertionError(
                    f"Please provide all correct details to run testcase :- Login With Wrong Credentials")

        except Exception as e:
            raise AssertionError(f"Error occurred: {e}")
        finally:
            self.driver.quit()