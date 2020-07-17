from selenium import webdriver
from selenium.webdriver import ActionChains


class Hover_selectproduct:
    def __init__(self, driver):
        self.drive = driver

    # write webelemet location
    hover_electronics = "//span[text()='Electronics']"
    samsung = "//li/a[text()='Samsung']"
    click_product = "(//div/a[@class='_2cLu-l'])[1]"

    def get_electronics(self):
        action = ActionChains(self.drive)
        hover = self.drive.find_element_by_xpath(self.hover_electronics)

        return action.move_to_element(hover).perform()

    def get_samsung(self):
        action = ActionChains(self.drive)
        samsung = self.drive.find_element_by_xpath(self.samsung)
        action.move_to_element(samsung).perform()

        return action.move_to_element(samsung).click().perform()

    def isfirsthoverpagedisplay(self):
        return self.get_electronics().is_displayed()

    def issubpagehoverdisplay(self):
        return self.get_samsung().is_displayed()


    # def get_samsungmodel(self):
    #     return self.drive.find_element_by_xpath(self.click_product)
    #
    # def hover_webelement(self):
    #     action = ActionChains(self.drive)
    #     action.move_to_element(self.get_electronics).click().perform()
    #
    # def hover_samsug(self):
    #     action = ActionChains(self.drive)
    #     action.move_to_element(self.get_samsung()).click().perform()
