import allure
import pytest

from allure_commons.types import AttachmentType

from utilities.excel_reader import get_list_from_excel


# def attach_screenshot(driver):
#     allure.attach(driver.get_screenshot_as_png(), name='test_check_for_login_cred.png',
#                   attachment_type=AttachmentType.PNG)

from demowebshop.POM.homepage import HomePage
from demowebshop.POM.loginpage import LogIn
# usernames=[("reddyvinuth27@gmail.com","selenium"), ("abc@yahoo.com","987654"),("xyz@gmail.com","123456"),("mno@abc.com","hello")]

credentials = get_list_from_excel("creds.xlsx","login_creds")
@pytest.mark.parametrize("username,password",credentials)
def test_login_with_proper_credentials(driver,username,password):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application(username, password)
    condition = driver.find_element("xpath", f"//a[.='{username}']").is_displayed()
    if not condition:
        allure.attach(driver.get_screenshot_as_png(), name='test_check_for_login_cred.png', attachment_type=AttachmentType.PNG)
    assert condition



@pytest.mark.skip
def test_login_without_password(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application(username="reddyvinuth27@gmail.com", password=" ")
    assert driver.find_element("xpath","//span[contains(.,'Login was unsuccessful.')]").is_displayed()
@pytest.mark.skip
def test_login_without_username(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application(username=" ", password="selenium")
    assert driver.find_element("xpath","//span[contains(.,'Login was unsuccessful.')]").is_displayed()
@pytest.mark.skip
def test_login_without_username_and_password(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application(username=" ", password=" ")
    assert driver.find_element("xpath","//span[contains(.,'Login was unsuccessful.')]").is_displayed()

@pytest.mark.skip
def test_login_with_improper_credentials(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application(username="radhikaamaresh2@gmail.com", password="123456")
    assert driver.find_element("xpath","//span[contains(.,'Login was unsuccessful.')]").is_displayed()