#!/usr/bin/env python
# -*- coding:utf-8 -*-
from client.conf import settings
import os
from .plugins import pack
#agent形式
#1.采集资产
#2.将资产数据发送到api(post)

#ssh形式
#1获取今日未采集的主机列表
#2.采集资产
#3.将资产数据发送到api(post)


#salt形式
#1获取今日未采集的主机列表
#2.采集资产
#3.将资产数据发送到api(post)

class BaseClient(object):
    def send_data(self,data_dic):
        pass

class SbaseClient(BaseClient):
    def get_host(self):
        pass

class Agent(BaseClient):
    def file_host(self):
        if not os.path.exists(settings.NIC_PATH):
            return None
        with open(settings.NIC_PATH,mode='r') as f:
            data = f.read()
        if not data:
            return None
        data = data.strip()
        return data
        # f = open('nid')
        # data = f.read()
        # f.close()
        # if data:
        #     return data
    def process(self):
        #1 采集资产

        data_dic = pack()
        # hostname = self.file_host()
        # if hostname:
        #     data_dic['hostname']=hostname
        # else:
        #     #获取当前主机名
        #     #写入nid文件
        #     data_dic['hostname']="adasdasdasd"
        # #2 将资产数据发送到API(post)
        # self.send_data(data_dic)

class SSH(SbaseClient):
    def process(self):
        data_dic = pack()
        # #获取今日未采集的主机列表
        # host_list = self.get_host()
        # for host in host_list:
        #     #采集资产
        #     data_dic = {}
        #     self.send_data(data_dic)


class Salt(SbaseClient):
    def process(self):
        #获取今日未采集的主机列表
        host_list = self.get_host()
        for host in host_list:
            #采集资产
            data_dic = {}
            self.send_data(data_dic)