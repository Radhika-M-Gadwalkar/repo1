from demowebshop.POM.homepage import HomePage
from utilities.locators import LoginPageLocators

class LogIn(HomePage,LoginPageLocators):

    def login_to_the_application(self, username,password):
        self.send_text_to_an_element(self.email_locator, username)
        self.send_text_to_an_element(self.password_locator,password)
        self.click_on_an_element(self.login_button)