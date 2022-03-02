import time
import sys
import os
from src.SimBrowser.Browser import Browser

def getUrls():
    urlsStr = ""
    # 从环境变量中获取
    envUrlsStr = os.getenv('URLS')
    urlsStr = envUrlsStr
    # 从命令行参数中获取
    if len(sys.argv) >= 2:
        argUrlsStr = sys.argv[1]
        if len(argUrlsStr) > 0:
            urlsStr = argUrlsStr
    urls = urlsStr.splitlines()

    return urls


browser = Browser("../tools/chromedriver")
browser.add_cookie({
        "domain":".bilibili.com",
        "name": cookie,
        "value":tbCookies[cookie],
        "path":'/',
        "expires":None
})

urls = getUrls()
urlsLen = len(urls)
print('一共有: ' + str(urlsLen) + ' 条URL')
for i in range(0, urlsLen):
    time.sleep(5)

    browser.goUrl(urls[i])
    browser.screenshot()
    print('截图成功: ' + urls[i])


    
print('运行完成')