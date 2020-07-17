import pytest
import time
from selenium import webdriver
from pages.product_details import Productdetails
from pages.product_select import Hover_selectproduct


@pytest.mark.usefixtures("onetime_setup")
class Testproductdetails:
    def test_verify_producttitle(self):
        hover = Hover_selectproduct(self.driver)
        hover.get_electronics()
        time.sleep(2)
        hover.get_samsung()
        current_window = self.driver.current_window_handc
        self.driver.implicitly_wait(10)
        # time.sleep(8)

        selectproduct = Productdetails(self.driver)
        selectproduct.getproduct()
        time.sleep(2)
        windows_list = self.driver.window_handles
        for window in windows_list:
            if window != current_window:
                self.driver.switch_to.window(window)
        producttitle = selectproduct.getproduct_title()
        # assert producttitle == True
        print(producttitle)

    def test_add_product(self):
        hover = Hover_selectproduct(self.driver)
        hover.get_electronics()
        time.sleep(2)
        hover.get_samsung()
        current_window = self.driver.current_window_handle
        self.driver.implicitly_wait(10)
        # time.sleep(8)

        selectproduct = Productdetails(self.driver)
        selectproduct.getproduct()
        time.sleep(2)
        windows_list = self.driver.window_handles
        for window in windows_list:
            if window != current_window:
                self.driver.switch_to.window(window)
        selectproduct.getproductincard()
        assert selectproduct.isaddcardpagedisplay()
