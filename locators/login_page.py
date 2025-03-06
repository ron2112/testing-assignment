from selenium.webdriver.common.by import By

class LoginPage:
    email_locator = (By.ID, "email")
    password_locator = (By.ID, "password")
    login_button_locator = (By.CLASS_NAME, "btnSubmit")
    login_error_locator = (By.CLASS_NAME, "help-block")