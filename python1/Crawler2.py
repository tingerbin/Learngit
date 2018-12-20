#!/usr/bin/env python3
#-*- conding=utf-8 -*-

import requests

response = requests.get('http://www.baidu.com')

print(response.status_code)
print(response.url)
print(response.headers)
print(response.cookies)
print(response.text)
print(response.content)
