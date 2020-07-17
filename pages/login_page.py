
class Login:
    def __init__(self, driver):
        self.driver = driver

    username = "//form/div/input[@type='text']"
    password = "//input[@type='password']"
    login = "(//button[@type='submit'])[2]"

    def getusername_box(self):
        return self.driver.find_element_by_xpath(self.username)

    def getpassword_box(self):
        return self.driver.find_element_by_xpath(self.password)

    def getlogin(self):
        return self.driver.find_element_by_xpath(self.login)

    def enter_username(self):
        self.getusername_box().send_keys(9011335735)

    def enter_password(self):
        self.getpassword_box().send_keys('Testing@123')

    def click_loginbtn(self):
        self.getlogin().click()


