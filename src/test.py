import sys
import os

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

print(getUrls())    