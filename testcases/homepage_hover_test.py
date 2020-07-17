import pytest

from pages.product_select import Hover_selectproduct


@pytest.mark.usefixtures("onetime_setup")
class Testhoverproduct:

    def test_verify_hover_electronics(self):
        hover = Hover_selectproduct(self.driver)
        hover.get_electronics()
        assert hover.isfirsthoverpagedisplay() == True


    def test_verify_hover_samsung(self):
        hover = Hover_selectproduct(self.driver)
        hover.get_samsung()
        assert hover.issubpagehoverdisplay() == True

