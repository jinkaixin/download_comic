目前只支持动漫狂网站的漫画下载，网址为 https://www.cartoonmad.com
且只支持一本一本下载，不支持同时下载多本

要求
需要安装python最新版本，即3.x
需要安装lxml,BeautifulSoup和selenium模块
电脑上需要安装chrome，且需要配置好chromedriver

使用方法
使用前，需要去setting文件里更改两个地方
folder_path   代表存储路径，可以改成自己的，替换引号里的路径就行了，或者直接在d盘建立download文件夹就行
url        代表要下载的漫画网址，去网站上点开要下载的漫画，把网址复制过来替换掉引号里的就行
再运行download.py文件即可开始下载，动漫狂网站不翻墙的话下载速度会比较慢
