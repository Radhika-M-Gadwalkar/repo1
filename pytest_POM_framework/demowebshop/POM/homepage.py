from demowebshop.Lib.library import Base
from utilities.locators import HomePageLocators
class HomePage(Base,HomePageLocators):


    def click_on_login(self):
        self.click_on_an_element(self.login_link_locator)

    def click_on_register(self):
        self.click_on_an_element(self.register_link_locator)
