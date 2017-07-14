#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/18 0:29
# @Author  : GerryDeng
# @File    : 111.py
# @Software: PyCharm

# file name "search_taobao.py"
import sys
import webbrowser

keywords = sys.argv[1:]

url = "https://s.taobao.com/search?q="
for i in keywords:
    url += i + "+"
    print(url)
url = url[:-1] #remove the last '+''
print(url)
webbrowser.open(url)