from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys
import os

class Browser:

    def __init__(self, driver_path):
        self.chrome_options = Options()
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        self.chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(driver_path ,options=self.chrome_options)

    def goUrl(self, url):
        self.driver.get(url)

    def screenshot(self):
        width = self.driver.execute_script("return document.documentElement.scrollWidth")
        height = self.driver.execute_script("return document.documentElement.scrollHeight")
        self.driver.set_window_size(width, height)
        self.driver.save_screenshot(
            '../data/screenshots/' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '.png')

    def execute_script(self, script):
        return self.driver.execute_script(script)

    def get_cookies(self):
        return self.driver.get_cookies()

    def get_cookie(self, name):
        return self.driver.get_cookie(name)

    def add_cookie(self, cookie_dict):
        self.driver.add_cookie(cookie_dict)