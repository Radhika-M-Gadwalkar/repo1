from demowebshop.POM.homepage import HomePage
from demowebshop.POM.loginpage import LogIn


class Search(LogIn):
    search_box_locator=("id","small-searchterms")
    search_button_locator=("xpath","//input[@value='Search']")
    def search_for_items(self, text):
        self.send_text_to_an_element(self.search_box_locator, text)
        self.click_on_an_element(self.search_button_locator)



