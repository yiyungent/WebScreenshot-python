FROM python:3.8 AS base

RUN apt-get install unzip
RUN pip install selenium
# 安装 Chrome
# TODO: 固定 Chrome 版本
# 注意: Chrome 版本必须与 chromedriver 版本对应
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome*.deb
RUN apt-get install -f
# TODO: 输出Chrome版本, 失败
RUN echo /usr/bin/google-chrome --version
# 安装 chromedriver
RUN wget http://chromedriver.storage.googleapis.com/88.0.4324.96/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
# 为所有用户添加可执行权限 (对chromedriver文件)
RUN chmod a+x chromedriver
# 下面两行安装中文字体
RUN apt install -y --force-yes --no-install-recommends fonts-wqy-microhei
RUN apt install -y --force-yes --no-install-recommends ttf-wqy-zenhei


ENTRYPOINT ["python", "main.py"]