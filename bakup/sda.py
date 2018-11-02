#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import re
import sys


from bs4 import BeautifulSoup


hrlist =[]
list = range(1,50)
for i in list:
    url = 'http://f.p03.space/forumdisplay.php?fid=19&page=%s'%i
    ret = requests.get(url=url)
    ret.encoding = 'utf-8'
    soup = BeautifulSoup(ret.text,features="lxml")
    tag1 = soup.find_all(name='a')
    #print(str(tag1))
    word = '0551'
    pattern = re.compile(word)
    result = pattern.findall(str(tag1))
    if result:
        hrlist.append(tag1)
    # #re.findall('0551',tag)
    # #result = re.findall(word,tag1)
    # print(result)
print(hrlist)