# import allure
# from allure_commons.types import AttachmentType
#
# from demowebshop.POM.homepage import HomePage
#
# def attach_screenshot(driver):
#     allure.attach(driver.get_screenshot_as_png(), name='test_check_for_login.png', attachment_type=AttachmentType.PNG)
#
# def test_check_for_login(driver):
#     home_page_obj = HomePage(driver)
#     home_page_obj.click_on_login()
#     condition = driver.find_element("id","Email").is_displayed()
#     if condition == False:
#         attach_screenshot(driver)
#     assert condition
#     # allure.attach(driver.get_screenshot_as_png(),name='test_check_for_login.png',attachment_type=AttachmentType.PNG)
#
# def test_check_for_register(driver):
#     home_page_obj = HomePage(driver)
#     home_page_obj.click_on_register()
#     condition = not (driver.find_element("id","Email").is_displayed())
#     if condition == False:
#         attach_screenshot(driver)
#     assert condition