#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from modules.imgspider import IMGSpider
from modules.downloader import DownLoader

spider = IMGSpider()
# list = spider.get_baidu_img_dict(key_word='柯南')['thumb_url']
# d = DownLoader(url_list=list)
# d.download()
print(spider.get_bing_img_dict('柯南'))