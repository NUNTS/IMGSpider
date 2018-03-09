import requests
import time
import os


class DownLoader:
    def __init__(self, url_list, path='temp', ext_name='.jpg', sleep_time=1):
        self.url_list = url_list,
        self.path = path,
        self.ext_name = ext_name
        self.s = requests.session()
        self.sleep_time = sleep_time

    def download(self):
        count = 1
        if os.path.isdir(str(self.path)):
            pass
        else:
            os.mkdir(str(self.path))
        for url in self.url_list:
            with open(''.format(self.path + count + self.ext_name), 'wb')as img:
                img.write(self.s.get(url).content)
                count += 1
                time.sleep(1)
                print('downloading:{}'.format(url))
