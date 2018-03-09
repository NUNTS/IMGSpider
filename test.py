#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from modules.imgspider import IMGSpider
from modules.downloader import DownLoader

spider = IMGSpider()
list = spider.get_img_dict(key_word='爱乃娜美')['thumb_url']
d = DownLoader(url_list=list)
d.download()