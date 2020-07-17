from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome(
    executable_path='C:\\Users\Sanket\\Desktop\\framework_pom\\resources\\webdrivers\\chromedriver.exe')
driver.get("https://www.flipkart.com")
driver.maximize_window()
print(driver.title)

time.sleep(5)
action = ActionChains(driver)
username = driver.find_element_by_xpath("//form/div/input[@type='text']")
username.send_keys(9011335735)
password = driver.find_element_by_xpath("//input[@type='password']")
password_enter = password.send_keys('Testing@123')
loginbt = driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()

time.sleep(6)

# click_oncross = driver.find_element_by_xpath("(//button)[2]").click()
# time.sleep(5)
click_on_electronics = driver.find_element_by_xpath("//span[text()='Electronics']")
action.move_to_element(click_on_electronics).click().perform()
click_on_samsung = driver.find_element_by_xpath("//li/a[text()='Samsung']")
action.move_to_element(click_on_samsung).click().perform()
time.sleep(5)
click_samsug=driver.find_element_by_xpath("(//div[@class='_3liAhj _2Vsm67']//a)[3]").click()
# text_product = driver.find_element_by_class_name("_35KyD6")
# print(text_product.text)

current_window=driver.current_window_handle
# print(current_window)
windows_list=driver.window_handles
# print(windows_list)
for window in windows_list:
    time.sleep(2)
    if window != current_window:
        driver.switch_to.window(window)
        text_product = driver.find_element_by_class_name("_35KyD6")
        print(text_product.text)
        add_tocard=driver.find_element_by_xpath("//li/button").click()
        # time.sleep(5)
        # remove_card=driver.find_element_by_xpath("(//div[text()='Remove'])[12]").click()
        # time.sleep(2)
        # # alert=Alert(driver)
        # # driver.switch_to.alert()
        # remove_me=driver.find_element_by_xpath("//div[text()='Remove']")
        # remove_me.click()
        time.sleep(5)
        action = ActionChains(driver)
        click_forlogout = driver.find_element_by_xpath("(//div[@class='_1jcwFN _3dmQRh'])[1]")
        action.move_to_element(click_forlogout).perform()
        # time.sleep(3)
        click_logout = driver.find_element_by_xpath("(//li[@class='_1-qoxT']/a)[10]")
        action.move_to_element(click_logout).click().perform()


time.sleep(5)
driver.close()
driver.quit()

