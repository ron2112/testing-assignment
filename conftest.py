import pytest
from datetime import datetime
from pathlib import Path
from selenium import webdriver

from data.configuration import Configuration
from pageobjects.register_page_actions import RegisterPageActions
from utilities.utils import Utils


@pytest.fixture(scope="function")
def chrome_driver():
    def _chrome_driver(url):
        driver = webdriver.Chrome()
        driver.get(url)
        return driver
    yield _chrome_driver

@pytest.fixture(scope="function")
def fill_register_details(chrome_driver):
    driver = chrome_driver(Configuration.web_url + Configuration.register_url)
    register_page = RegisterPageActions(driver)

    register_page.send_first_name(Configuration.first_name)
    register_page.send_last_name(Configuration.last_name)
    register_page.select_date_of_birth(Configuration.date_of_birth)
    register_page.send_street(Configuration.street)
    register_page.send_postal_code(Configuration.postal_code)
    register_page.send_city(Configuration.city)
    register_page.send_state(Configuration.state)
    register_page.select_country(Configuration.country)
    register_page.send_phone(Configuration.phone_number)
    register_page.send_email(Utils.generate_random_email())
    register_page.send_password(Configuration.password)
    return driver

@pytest.fixture(scope="function")
def skip_register_details(chrome_driver):
    driver = chrome_driver(Configuration.web_url + Configuration.register_url)
    register_page = RegisterPageActions(driver)

    register_page.skip_first_name()
    register_page.skip_last_name()
    register_page.skip_email()
    register_page.skip_password()

    register_page.select_date_of_birth(Configuration.date_of_birth)
    register_page.send_street(Configuration.street)
    register_page.send_postal_code(Configuration.postal_code)
    register_page.send_city(Configuration.city)
    register_page.send_state(Configuration.state)
    register_page.select_country(Configuration.country)
    register_page.send_phone(Configuration.phone_number)
    return driver

@pytest.fixture(scope="function")
def check_invalid_email(chrome_driver):
    driver = chrome_driver(Configuration.web_url + Configuration.register_url)
    register_page = RegisterPageActions(driver)

    register_page.send_first_name(Configuration.first_name)
    register_page.send_last_name(Configuration.last_name)
    register_page.select_date_of_birth(Configuration.date_of_birth)
    register_page.send_street(Configuration.street)
    register_page.send_postal_code(Configuration.postal_code)
    register_page.send_city(Configuration.city)
    register_page.send_state(Configuration.state)
    register_page.select_country(Configuration.country)
    register_page.send_phone(Configuration.phone_number)
    register_page.send_email(Configuration.invalid_email)
    register_page.send_password(Configuration.password)
    return driver

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today = datetime.now()
    current_dir = Path(__file__).parent
    report_dir = current_dir / "reports" / today.strftime("%Y%m%d")

    # Ensure directory exists
    report_dir.mkdir(parents=True, exist_ok=True)

    # Define report path
    report_path = report_dir / f"Report_{today.strftime('%Y%m%d%H%M')}.html"

    # Set pytest-html options
    config.option.htmlpath = str(report_path)
    config.option.self_contained_html = True

def pytest_html_report_title(report):
    report.title = "Test Tool Shop Registration Test Report"