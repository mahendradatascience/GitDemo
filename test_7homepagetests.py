import unittest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
#from selenium.webdriver import ChromeOptions
#from __builtin__ import classmethod

class HomePageTest(unittest.TestCase):

    #Opening browser.
    @classmethod
    def setUpClass(cls):
        
        #cls.options = webdriver.ChromeOptions()
        #cls.options.add_experimental_option("detach", True)
        cls.service=Service(r'E:\Software_Testing\software\chromedriver.exe')
        #cls.driver = webdriver.Chrome(options=cls.options,service=cls.service)
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.get("https://www.amazon.in/")
        print("setUpClass executed")
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass executed")
        cls.driver.quit()
    def test_search_filled_exist(self): # cheak search field exit on home page
        try:
            self.driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
        except NoSuchElementException as exception:
            print("element not present")
            print("India employe mahendra  is changing code")
           
        

    def test_language_option_exist(self):
        # check language options dropdown on Home page
        try:
            self.driver.find_element(By.XPATH, "//div[normalize-space()='EN']")
        except NoSuchElementException as exception:
            print("element not present")
            print("mahendra is presenting")
        
    def test_shopping_cart_empty_message(self):
            # check content of My Shopping Cart block on Home page
        shopping_cart_icon =self.driver.find_element(By.XPATH, "//span[@id='nav-cart-count']").click()
        try:
            shopping_cart_status =self.driver.find_element(By.XPATH, "//h1[normalize-space()='Your Amazon Cart is empty.']").text
        except NoSuchElementException as exception:
            print("element not present")
            print("India employe new  is changing code")
    def test_shopping_cart_empty_message(self):
            # check content of My Shopping Cart block on Home page
        shopping_cart_icon =self.driver.find_element(By.XPATH, "//span[@id='nav-cart-count']").click()
        try:
            shopping_cart_status =self.driver.find_element(By.XPATH, "//h1[normalize-space()='Your Amazon Cart is empty.']").text
        except NoSuchElementException as exception:
            print("element not present")
            print("India employe new  is changing code")
    def test_shopping_cart_empty_message(self):
            # check content of My Shopping Cart block on Home page
        shopping_cart_icon =self.driver.find_element(By.XPATH, "//span[@id='nav-cart-count']").click()
        try:
            shopping_cart_status =self.driver.find_element(By.XPATH, "//h1[normalize-space()='Your Amazon Cart is empty.']").text
        except NoSuchElementException as exception:
            print("element not present")
            print("India employe new  is changing code")
            print("US employe new  is changing code")
            print("US employe new  is changing code")
    def test_search_filled_exist(self): # cheak search field exit on home page
        try:
            self.driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
        except NoSuchElementException as exception:
            print("element not present")
            print("India employe mahendra  is changing code")
    def test_search_filled_exist(self): # cheak search field exit on home page
        try:
            self.driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
        except NoSuchElementException as exception:
            print("element not present")
            print("India employe mahendra  is changing code")
           

           

##        print(shopping_cart_status)
##        self.assertEqual("Your Amazon Cart is empty.", shopping_cart_status)

##    def is_element_present(self, how, what):
##        # Utility method to check presence of an element on page
##        #:params how: By locator type
##        #:params what: locator value
##        try:
##            self.driver.find_element(by=how, value=what)
##        except NoSuchElementException as exception:
##            
##           print ("Web Element is not Available in the given Web Page.")

if __name__== '__main__':
    unittest.main(verbosity=2)
    
             
        
        
        
