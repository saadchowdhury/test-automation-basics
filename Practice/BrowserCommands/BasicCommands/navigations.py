from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class Navigate():
    def navigate_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get('https://www.google.com')

        time.sleep(2)

        driver.get('https://www.youtube.com')

        time.sleep(2)

        # this line of code returns to the previous page
        driver.back()

        time.sleep(1)

        # this line of code takes to the next page
        driver.forward()

        time.sleep(1)

        # this line of code opens a new tab
        driver.switch_to.new_window('tab 1')

        time.sleep(1)

        driver.switch_to.new_window('tab 2')
        driver.get('http://www.instagram.com')
        time.sleep(5)

obj = Navigate()
obj.navigate_demo()