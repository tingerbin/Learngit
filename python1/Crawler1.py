#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import urllib.parse
import urllib.request

#data=bytes(urllib.parse.urlencode({'word': 'hello'}),encoding='utf8')

response=urllib.request.urlopen('http://www.baidu.com')
html=response.read()
print(html)
