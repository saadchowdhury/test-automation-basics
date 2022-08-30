from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class Browser_Commands():

    def commands(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        # open url in browser
        driver.get('https://www.google.com')

        # full screen size
        # driver.maximize_window()
        # driver.fullscreen_window()
        # driver.set_window_size(400 , 400)
        max_win_size = driver.get_window_size()
        print(max_win_size)

        # title of the current page
        title = driver.title
        print(title)

        # url of the current page
        url = driver.current_url
        print(url)

        # delay for 5 sec
        time.sleep(1)

obj = Browser_Commands()
obj.commands()