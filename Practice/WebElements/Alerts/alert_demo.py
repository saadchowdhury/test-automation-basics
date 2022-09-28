from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Alert():
    def alert_automation(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/javascript_alerts')

        # normal alerts
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div/ul/li[1]/button').click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)


        # confirmation alert

        driver.find_element(By.XPATH, '/html/body/div[2]/div/div/ul/li[2]/button').click()
        time.sleep(2)
        driver.switch_to.alert.dismiss()
        time.sleep(2)

        # prompt alert
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div/ul/li[3]/button').click()
        driver.switch_to.alert.send_keys('testing in process')
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)
        driver.close()

obj = Alert()
obj.alert_automation()