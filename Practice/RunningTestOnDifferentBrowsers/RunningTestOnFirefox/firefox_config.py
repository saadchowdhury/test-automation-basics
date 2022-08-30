from selenium import webdriver

class Firefox():
    def firefox_launch(self):
        driver = webdriver.Firefox(executable_path="I:\\SQAautomation\\tools\\geckodriver-v0.31.0-win64\\geckodriver.exe")
        driver.close()


testobj = Firefox()
testobj.firefox_launch()
