from selenium.webdriver.common.by import By

class RegisterPage:
    first_name_locator = (By.ID, "first_name")
    last_name_locator = (By.ID, "last_name")
    date_of_birth_locator = (By.ID, "dob")
    street_locator = (By.ID, "street")
    postal_code_locator = (By.ID, "postal_code")
    city_locator = (By.ID, "city")
    state_locator = (By.ID, "state")
    country_locator = (By.ID, "country")
    phone_number_locator = (By.ID, "phone")
    email_locator = (By.ID, "email")
    password_locator = (By.ID, "password")
    register_button_locator = (By.XPATH, "//button[@data-test='register-submit']")
    # error and warning locators
    password_detection_locator = (By.XPATH, "//div[@class='fill weak']")
    first_name_blank_locator = (By.XPATH, "//div[@data-test='first-name-error']")
    last_name_blank_locator = (By.XPATH, "//div[@data-test='last-name-error']")
    email_blank_locator = (By.XPATH, "//div[@data-test='email-error']")
    password_blank_locator = (By.XPATH, "//div[@data-test='password-error']")
    register_error_locator = (By.XPATH, "//div[@class='help-block']")