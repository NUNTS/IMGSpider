import re


def url_match():
    # 匹配所有url
    p = re.compile(r'[a-z]+://[a-zA-Z0-9.,&%?;=/_-]+')
    return p


def greedy_url_match():
    # 匹配所有url，包括反斜杠
    p = re.compile(r'[a-z]+:/\\*[a-zA-Z0-9.,&%?;=\\/_-]+')
    return p
