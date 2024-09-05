from demowebshop.POM.homepage import HomePage


class  Register(HomePage):
    gender_locator = ("xpath","//div[@class='gender']//label[.='Female']")
    first_name_locator = ("id","FirstName")
    last_name_locator = ("id","LastName")
    email_locator = ("id","Email")
    password_locator = ("id","Password")
    confirm_password_locator = ("id","ConfirmPassword")
    register_button_locator = ("xpath","//input[@id='register-button']")
    def register_to_the_application(self, first_name, last_name, email, password, confirm_password):
        self.click_on_an_element(self.gender_locator)
        self.send_text_to_an_element(self.first_name_locator, first_name)
        self.send_text_to_an_element(self.last_name_locator, last_name)
        self.send_text_to_an_element(self.email_locator, email)
        self.send_text_to_an_element(self.password_locator, password)
        self.send_text_to_an_element(self.confirm_password_locator, confirm_password)
        self.click_on_an_element(self.register_button_locator)