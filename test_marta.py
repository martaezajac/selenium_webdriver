# -*- coding: utf-8 -*-
import unittest
from time import sleep
from selenium import webdriver

class WsbPlCheck(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()

    def test_wsb(self):
        driver=self.driver
        driver.get("http://wsb.pl/wroclaw")
        driver.maximize_window
        podyplomowe_link=driver.find_element_by_link_text("Studia podyplomowe")
        podyplomowe_link.click()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)
