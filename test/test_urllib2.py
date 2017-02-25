#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib
import http.cookiejar
from urllib import request
url = "http://www.baidu.com"

print("The First Method")
response1 = request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))


print("The Second Method")
req = request.Request(url)
req.add_header("user-agent", "Mozilla/5.0")
response2 = request.urlopen(req)
print(response2.getcode())
print(len(response2.read()))


print("The Third Method")
cj = http.cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj))
request.install_opener(opener)
response3 = request.urlopen(url)
print(response3.getcode())
print(cj)
print(response3.read())