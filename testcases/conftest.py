
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest

from pages.login_page import Login


@pytest.fixture(scope="class")
def onetime_setup(request):
    driver = webdriver.Chrome(
        executable_path='C:\\Users\Sanket\\Desktop\\framework_pom\\resources\\webdrivers\\chromedriver.exe')
    # action = ActionChains(driver)
    driver.get("https://www.flipkart.com")
    driver.maximize_window()
    # login=Login(driver)
    # login.enter_username()
    # login.enter_password()
    # login.click_loginbtn()
    # username=driver.find_element_by_xpath("//form/div/input[@type='text']")
    # username.send_keys(9011335735)
    # password = driver.find_element_by_xpath("//input[@type='password']")
    # password.send_keys('Testing@123')
    click_oncross = driver.find_element_by_xpath("(//button)[2]").click()
    driver.implicitly_wait(10)
    request.cls.driver = driver

    yield driver
    time.sleep(10)
    driver.close()
    driver.quit()
# @pytest.fixture(scope="class")
# def setup():
#     print("path of browser1")