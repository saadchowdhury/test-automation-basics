from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Webelements():

    def basic_commands(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get('https://opensource-demo.orangehrmlive.com/')

        # locate webelements

        username = driver.find_element(By.ID, 'txtUsername')
        password = driver.find_element(By.ID, 'txtPassword')
        login_btn = driver.find_element(By.ID, 'btnLogin')

        # login Action
        username.send_keys('Admin')
        password.send_keys('admin123')
        login_btn.click()

        time.sleep(5)

        driver.close()

obj = Webelements()
obj.basic_commands()