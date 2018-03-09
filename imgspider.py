import re
import requests
import json

from downloader import DownLoader as d
from util import header


class IMGSpider:
    def __init__(self):
        self.url = 'https://image.baidu.com/search/index?tn=baiduimage&word='
        self.s = requests.session()
        self.s.headers = header.get_header()
        self.img_dict = {}

    def get_img_dict(self, key_word=''):
        # 缩略图
        thumb = re.compile(r'("thumbURL":"[a-z]+:[/+\\][\w.,&%?;=\\/_-]+)')
        # 大图
        obj = re.compile(r'("objURL":"[a-z]+:[/+\\][\w.,&%?;=\\/_-]+)')
        doc = self.s.get(self.url + key_word).text
        thumb_url = thumb.findall(doc)
        obj_url = obj.findall(doc)
        # 缩略图
        for i in thumb_url.copy():
            thumb_url[thumb_url.index(i)] = (i.replace('\\', '').replace('"thumbURL":"', ''))
        # 大图
        for i in obj_url.copy():
            obj_url[obj_url.index(i)] = (i.replace('\\', '').replace('"objURL":"', ''))
        self.img_dict['thumb_url'] = thumb_url
        self.img_dict['obj_url'] = obj_url
        return self.img_dict

    def sav_img_dict(self, key_word=''):
        res = self.get_img_dict(key_word)
        with open('temp.json', 'w', encoding='utf-8') as u:
            json.dump(res, u)


if __name__ == '__main__':
    img = IMGSpider()
    print(img.get_img_dict('美食')['obj_url'])
    d = d(url_list=img.get_img_dict('美食')['obj_url'])
    d.download()
