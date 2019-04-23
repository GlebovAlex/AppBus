#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by  import By
from selenium.webdriver.chrome.options import Options
import unittest
import time

class Login(unittest.TestCase):

    def setUp(self):
        global driver
        options = Options()
        options.headless = True
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.binary_location = '/usr/bin/google-chrome'
        driver = webdriver.Chrome(options=options, executable_path='/usr/bin/chromedriver')
        driver.get("https://www.gmail.com")
        driver.maximize_window()

    def test_Login(self):
        driver.find_element_by_xpath("//input[@type='email']").send_keys("u2.qallab@gmail.com")
        print("found the input field , success")
    
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
