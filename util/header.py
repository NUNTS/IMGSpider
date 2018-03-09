#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from random import randint

ua_desktop_text = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                  'Chrome/64.0.3282.140 Safari/537.36\n' \
                  'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0\n' \
                  'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; ' \
                  '.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)\n' \
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 ' \
                  '(KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
ajax_header = {'X-Requested-With': 'XMLHttpRequest'}
keep = {'Connection': 'keep-alive'}


def get_header():
    h = {}
    ua_arr = ua_desktop_text.split('\n')
    h['User-Agent'] = ua_arr[randint(0, ua_arr.__len__()) - 1]
    return h


def get_ajax_header():
    h = get_header()
    h.update(ajax_header)
    return h


def get_keep_header():
    h = get_header()
    h.update(keep)
    return h

