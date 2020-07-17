
class Productdetails:
    def __init__(self ,driver):
        self.driver = driver

    # write webelement location
    click_product = "(//div[@class='_3liAhj _2Vsm67']//a)[3]"
    product_idfor_text = "_35KyD6"

    add_to_card ="//li/button"

    def select_product(self):
        return self.driver.find_element_by_xpath(self.click_product)

    def getProducttextFromProductDetailPage(self):
        return self.driver.find_element_by_class_name(self.product_idfor_text)

    def addproductoncard(self):
        return self.driver.find_element_by_xpath(self.add_to_card)

    def getproduct(self):
        return self.select_product().click()

    def getproduct_title(self):
        return self.getProducttextFromProductDetailPage().text
    def getproductincard(self):
        return self.addproductoncard().click()

    def isaddcardpagedisplay(self):
        return self.getproductincard()




