from selenium import webdriver


class Chrome():

    def chrome_launch(self):
        driver = webdriver.Chrome(executable_path="I:\\SQAautomation\\tools\\chromedriver_win32\\chromedriver.exe")



obj = Chrome()
obj.chrome_launch()

