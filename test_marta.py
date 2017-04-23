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
        search_box=driver.find_element_by_id("edit-search-block-form--2")
        search_box.send_keys("tester")
        search_box.submit()
        sleep(4)
        results=driver.find_elements_by_class_name("search-result")

        print ("Znalazlem " + str(len(results))+ " wyników na tej stronie:\n")

        for result in results:
            print(result.text +"\n")
        self.assertEqual(10,len(results))

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)
