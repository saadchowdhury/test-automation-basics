from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Webelements():

    def basic_commands(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get('https://www.facebook.com/')

        forgot_pass = driver.find_element(By.LINK_TEXT, 'Forgotten password?')
        print(forgot_pass.text)

        username = driver.find_element(By.ID, 'email')
        password = driver.find_element(By.ID, 'pass')
        login_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')

        # size
        username_size = username.size
        print(username_size)
        print('height is : ' + str(username_size['height']))
        print('width is : ' + str(username_size['width']))

        username.send_keys('saadchowdhury007@gmail.com')
        password.send_keys('hello')
        time.sleep(2)
        password.clear()
        password.send_keys('123456')
        login_btn.click()


        time.sleep(10)
        driver.close()

obj = Webelements()
obj.basic_commands()