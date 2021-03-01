from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys
import os

def getUrls():
    urlsStr = ""
    # 从环境变量中获取
    envUrlsStr = os.getenv('URLS')
    urlsStr = envUrlsStr
    # 从命令行参数中获取
    argUrlsStr = sys.argv[1]
    if len(argUrlsStr) > 0:
        urlsStr = argUrlsStr
    urls = urlsStr.splitlines()

    return urls

def save_screenshot(url):
    driver.get(url)
    width = driver.execute_script("return document.documentElement.scrollWidth")
    height = driver.execute_script("return document.documentElement.scrollHeight")
    driver.set_window_size(width, height)
    driver.save_screenshot('./screenshots/' + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) +'.png')
    
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
driver = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)

urls = getUrls()
urlsLen = len(urls)
print('一共有: ' + str(urlsLen) + ' 条URL')
for i in range(1, urlsLen):
    time.sleep(5)
    save_screenshot(urls[i])
    print('截图成功: ' + urls[i])
    
print('运行完成')