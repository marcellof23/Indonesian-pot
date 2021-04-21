import pytest
import sys
import os
from marketController import searchProductByTitleController, searchProductByCategoryController


class TestMarket:
    def test_marketOne(self):
        product = searchProductByTitleController("eceng")
        assert product[0]['title'] == "eceng gondok"

    def test_marketTwo(self):
        product = searchProductByTitleController("haha")
        assert len(product) == 0

    def test_marketThree(self):
        product = searchProductByCategoryController("Tanaman Hias")
        assert product[1]['title'] == "kaktus"

    def test_marketFour(self):
        product = searchProductByTitleController("Tanaman Langka")
        assert len(product) == 0
