from selenium.webdriver.common.by import By


class LoginPage:
    URL = "https://www.strava.com/login"

    # Locators
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def set_email(self, email):
        email_input = self.driver.find_element(*self.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)

    def set_password(self, password):
        password_input = self.driver.find_element(*self.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

    def click_login(self):
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()
