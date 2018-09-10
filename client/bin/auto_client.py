#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os,sys
# from client.src.plugins import disk  #导入py文件
# from client.src import plugins  #内部加载plugins 的__init__.py文件
# #BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# BASEDIR = os.path.dirname(os.path.abspath(__file__))
#
# sys.path.append(BASEDIR)
# data_dic = plugins.pack()
import requests
import json

from client.src.plugins.salt_test01 import celedata


if __name__ == "__main__":
    data = celedata()
    #print(data)
    data = {'hostname':'node2','data':
        {'Server': {'hostname': 'node2', 'manage_ip': '172.17.1.199', 'os_platform': 'CentOS Linux-7', 'os_version': '7.4.1708', 'cpu_model': 'Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz', 'cpu_count': 1},
                    'Disk':{'DISKslot#0':{'capacity': '40.5GB','slot':'DISKslot#0'}},
                    'Memory': {'RAM slot #0': {'capacity': '2024 MB', 'slot': 'RAM slot #0', 'model': 'DRAM', 'speed': 'Unknown', 'manufacturer': 'Not Specified', 'sn': 'Not Specified'}},
                    'NIC':{'ens33': {'name': 'ens33', 'hwaddr': '00:0c:29:a1:2e:67', 'up': False, 'netmask': '255.255.255.0', 'ipaddrs': '172.17.1.199'}}}}
    data = json.dumps(data)
    #print(data)
    url = "http://127.0.0.1:8000/api/asset-data/"
    ret = requests.post(url=url,data=data)
    print(ret.content)