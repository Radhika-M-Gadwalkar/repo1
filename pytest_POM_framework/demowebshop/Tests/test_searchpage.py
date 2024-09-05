# from demowebshop.POM.homepage import HomePage
# from demowebshop.POM.loginpage import LogIn
# from demowebshop.POM.searchpage import Search
#
#
# def test_search_for_items(driver):
#     value= "laptop"
#     home = HomePage(driver)
#     home.click_on_login()
#     login = LogIn(driver)
#     login.login_to_the_application(username="reddyvinuth27@gmail.com", password="selenium")
#     assert driver.find_element("xpath","//a[.='reddyvinuth27@gmail.com']").is_displayed()
#     search = Search(driver)
#     search.search_for_items(text=value)
#     assert driver.find_element("xpath",f"//input[@value='{value}']").is_displayed()