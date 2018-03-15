#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import re
import requests
import json

from util.header import get_header


class IMGSpider:
    def __init__(self):
        self.baidu_url = 'https://image.baidu.com/search/index?tn=baiduimage&word='
        self.bing_url = 'http://cn.bing.com/images/search?q='
        self.s = requests.session()
        self.s.headers = get_header()
        self.img_dict = {}

    def get_baidu_img_dict(self, key_word=''):
        # 缩略图
        thumb = re.compile(r'("thumbURL":"[a-z]+:[/+\\][\w.,&%?;=\\/_-]+)')
        # 大图
        obj = re.compile(r'("objURL":"[a-z]+:[/+\\][\w.,&%?;=\\/_-]+)')
        doc = self.s.get(self.baidu_url + key_word).text
        thumb_url = thumb.findall(doc)
        obj_url = obj.findall(doc)
        # 缩略图
        for i in thumb_url.copy():
            thumb_url[thumb_url.index(i)] = (
                i.replace('\\', '').replace('"thumbURL":"', ''))
        # 大图
        for i in obj_url.copy():
            obj_url[obj_url.index(i)] = (
                i.replace('\\', '').replace('"objURL":"', ''))
        self.img_dict['thumb_url'] = thumb_url
        self.img_dict['obj_url'] = obj_url
        return self.img_dict

    def get_bing_img_dict(self,key_word=''):
        """
        ensearch=1: 启用英文页面
        first=1: 第一页
        cw,ch: 屏幕宽高
        """
        doc = self.s.get(url=self.bing_url+key_word).text
        with open('bing.html','w', encoding='utf-8') as bing:
            bing.write(doc)
        return doc

