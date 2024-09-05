# from demowebshop.POM.homepage import HomePage
# from demowebshop.POM.registerpage import Register
#
#
# def test_register_with_proper_inputs(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_to_the_application(first_name="Radhika", last_name="Amaresh", email="radhikaamaresh@live.com", password="radhika02", confirm_password="radhika02")
#     assert driver.find_element("xpath","//a[.='radhikaamaresh@live.com']").is_displayed()
#
#
# def test_register_without_first_name(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_to_the_application(first_name=" ", last_name="Amaresh", email="radhikaamaresh@live.com", password="radhika02", confirm_password="radhika02")
#     assert driver.find_element("xpath","//span[.='First name is required.']").is_displayed()
#
# def test_register_without_last_name(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_to_the_application(first_name="Radhika", last_name=" ", email="radhikaamaresh@live.com", password="radhika02", confirm_password="radhika02")
#     assert driver.find_element("xpath", "//span[.='Last name is required.']").is_displayed()
#
# def test_register_without_email(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_to_the_application(first_name="Radhika", last_name="Amaresh", email=" ", password="radhika02", confirm_password="radhika02")
#     assert driver.find_element("xpath", "//span[.='Email is required.']").is_displayed()
#
# def test_register_with_insufficient_email(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_to_the_application(first_name="Radhika", last_name="Amaresh", email="radhikaamaresh", password="radhika02", confirm_password="radhika02")
#     assert driver.find_element("xpath", "//span[.='Wrong email']").is_displayed()
#
# def test_register_with_existing_email(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_to_the_application(first_name="Radhika", last_name="Amaresh", email="radhikaamaresh@live.com", password="radhika02", confirm_password="radhika02")
#     assert driver.find_element("xpath", "//li[.='The specified email already exists']").is_displayed()
#
# def test_register_without_password(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_to_the_application(first_name="Radhika", last_name="Amaresh", email="radhikaamaresh@live.com ", password=" ", confirm_password="radhika02")
#     assert driver.find_element("xpath", "//span[.='Password is required.']").is_displayed()
#
# def test_register_with_insufficient_password(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_to_the_application(first_name="Radhika", last_name="Amaresh", email="radhikaamaresh@live.com ", password="rad", confirm_password="radhika02")
#     assert driver.find_element("xpath", "//span[.='The password should have at least 6 characters.']").is_displayed()
#
# def test_register_without_confirm_password(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_to_the_application(first_name="Radhika", last_name="Amaresh", email="radhikaamaresh@live.com ", password="radhika02", confirm_password=" ")
#     assert driver.find_element("xpath", "//span[.='Password is required.']").is_displayed()
#
# def test_register_with_mismatched_confirm_password(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_to_the_application(first_name="Radhika", last_name="Amaresh", email="radhikaamaresh@live.com ", password="radhika02", confirm_password="123456")
#     assert driver.find_element("xpath", "//span[.='The password and confirmation password do not match.']").is_displayed()
#
#
#
