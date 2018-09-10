#!/usr/bin/env python
# -*- coding:utf-8 -*-
from cmdb import models
import time,datetime
from .api_test_set import get_in,get_exclude
#服务器的跟新
class Server_data_info(object):
    @staticmethod
    def data_change(server_obj,server_info):
        try:
            log_list = []
            server_data = server_info['data']['Server']
            #判断系统的变更
            if server_obj.os_platform != server_data['os_platform']:
                log_list.append("系统由%s变为%s"%(server_obj.os_platform,server_data['os_platform']))
                server_obj.os_platform = server_data['os_platform']
            #判断系统版本的变化
            if server_obj.os_version != server_data['os_version']:
                log_list.append("系统版本由%s变成%s"%(server_obj.os_version,server_data['os_version']))
                server_obj.os_version = server_data['os_version']
            #判断cpu型号是否有变化
            if server_obj.cpu_model != server_data['cpu_model']:
                log_list.append("cpu型号由%s变成%s"%(server_obj.cpu_model,server_data['cpu_model']))
                server_obj.cpu_model = server_data['cpu_model']
            #判断cpu的个数
            if server_obj.cpu_count != server_data['cpu_count']:
                log_list.append("cpu个数由%s变成%s"%(server_obj.cpu_count,server_data['cpu_count']))
                server_obj.cpu_count = server_data['cpu_count']
            #判断管理ip，我这里用的是服务器的ip地址代替
            if server_obj.manage_ip != server_data['manage_ip']:
                log_list.append("管理IP由%s变成%s"%(server_obj.manage_ip,server_data['manage_ip']))
                server_obj.manage_ip = server_data['manage_ip']

            server_obj.save()
            if log_list:
                models.AssetRecord.objects.create(asset_obj=server_obj.asset,
                                                  content = ';'.join(log_list))
        except Exception as e:
            models.ErrorLog.objects.create(asset_obj=server_obj,title='出错',content="出错啦 sssss")

    @staticmethod
    def update_aseet_lasttime(server_obj):
        try:
            current_time = datetime.date.today()
            server_obj.asset.latest_date = current_time
            server_obj.save()
            models.AssetRecord.objects.create(asset_obj=server_obj.asset,content='资产汇报')

        except Exception as e:
            models.ErrorLog.objects.create(asset_obj=server_obj.asset, title='basic-run',
                                           content="chucuo a s das da sdas")

#网卡的跟新，删除，添加
class Nic_data_info(object):
    @staticmethod
    def nic_data(server_obj,server_info):
        try:
            cli_nic_data = server_info['data']['NIC']
            nic_obj = models.NIC.objects.filter(server_obj=server_obj)

            nic_list = list(map(lambda x:x,(item.name for item in nic_obj)))
            update_list = get_in(set(cli_nic_data.keys()),set(nic_list))
            ######print('update_list',update_list)
            add_list = get_exclude(set(cli_nic_data.keys()),update_list)
            ######print("add_list",add_list)
            del_list = get_exclude(nic_list,update_list)
            #######print('del_list',del_list)
            Nic_data_info.nic_add(add_list,cli_nic_data,server_obj)
           # print('执行。。。。。。。')
            Nic_data_info.nic_del(del_list,nic_obj,server_obj)
            Nic_data_info.nic_update(update_list,nic_obj,cli_nic_data,server_obj)

        except Exception as e:
            models.ErrorLog.objects.create(asset_obj=server_obj.asset, title='nic-run', content='chucuolea s ')
    #添加网卡，
    @staticmethod
    def nic_add(add_list,cli_nic_data,server_obj,):
        for item in add_list:
            #print('---->',item)
            #print('----->>>>>',cli_nic_data)
            add_nic_dic = cli_nic_data[item]
            #print('______###',add_nic_dic)
            nic_log = '[新增网卡]{name}:mac地址为{hwaddr};状态为{up};掩码为{netmask};IP地址为{ipaddrs}'.format(**add_nic_dic)
            #print(nic_log)
            add_nic_dic['server_obj'] = server_obj

            models.NIC.objects.create(**add_nic_dic)
            models.AssetRecord.objects.create(asset_obj=server_obj.asset, content=nic_log)
    #删除网卡
    @staticmethod
    def nic_del(del_list,nic_obj,server_obj):
        for item in nic_obj:
            if item.name in del_list:
                #print(item.__dict__)
                nic_log = '[移除网卡]{name}:mac地址为{hwaddr};状态为{up};掩码为{netmask};IP地址为{ipaddrs}'.format(**item.__dict__)
                #print(nic_log)
                item.delete()
                models.AssetRecord.objects.create(asset_obj=server_obj.asset, content=nic_log)
    #更新网卡
    @staticmethod
    def nic_update(update_list,nic_obj_list,cli_nic_data,server_obj):
        for item in nic_obj_list:
            if item.name in update_list:
                nic_update_log = []
                new_hwaddr = cli_nic_data[item.name]['hwaddr']
                if item.hwaddr != new_hwaddr:
                    nic_update_log.append("[更新网卡]%s:mac地址由%s变更为%s"%(item.name,item.hwaddr,new_hwaddr))
                    item.hwaddr = new_hwaddr
                new_up = cli_nic_data[item.name]['up']
                if item.up != new_up:
                    nic_update_log.append("[更新网卡]%s:状态由%s变更为%s"%(item.name,item.up,new_up))
                    item.up = new_up

                new_netmask = cli_nic_data[item.name]['netmask']
                if item.netmask !=new_netmask:
                    nic_update_log.append("[更新网卡]%s:子网掩码由%s变更为%s"%(item.name,item.netmask,new_netmask))
                    item.netmask = new_netmask

                new_ipaddrs = cli_nic_data[item.name]['ipaddrs']
                if item.ipaddrs != new_ipaddrs:
                    nic_update_log.append("[更新网卡]%s:ip地址由%s变更为%s"%(item.name,item.ipaddrs,new_ipaddrs))
                    item.ipaddrs = new_ipaddrs

                item.save()
                if nic_update_log:
                    models.AssetRecord.objects.create(asset_obj=server_obj.asset, content=nic_update_log)

#内存的更新，删除，添加
class Mem_data_info(object):
    @staticmethod
    def Mem_data(server_obj,server_info):
        try:
            cli_mem_data = server_info['data']['Memory']#客户端汇报的内存信息
            mem_obj = models.Memory.objects.filter(server_obj=server_obj)#获取当前的主机内存的对象
            #print('mem_obj',mem_obj)
            mem_list = list(map(lambda x:x,(item.slot for item in mem_obj))) #获得数据库中的内存
            mem_update_list = get_in(set(mem_list),set(cli_mem_data.keys()))#更新的内存
            #print('mem_update_list',mem_update_list)
            mem_del_list = get_exclude(mem_list,mem_update_list)#删除的内存
            mem_add_list = get_exclude(set(cli_mem_data.keys()),mem_update_list)#添加的内存
            #print('mem_add_list',mem_add_list)


            Mem_data_info.mem_update(mem_update_list,mem_obj,server_obj,cli_mem_data)
            Mem_data_info.mem_del(mem_del_list,mem_obj,server_obj)

            Mem_data_info.mem_add(mem_add_list,cli_mem_data,server_obj)

        except Exception as e:
            models.ErrorLog.objects.create(asset_obj=server_obj.asset,title='错误',content="出现错误，测试")

    @staticmethod   #删除内存方法
    def mem_del(mem_del_list,mem_obj,server_obj):
        for item in mem_obj:
            if item.slot in mem_del_list:
                log_str = '[移除内存]插槽为{slot};容量为{capacity};类型为{model};速度为{speed};厂商为{manufacturer};SN号为{sn}'.format(
                    **item.__dict__)
                item.delete()
                models.AssetRecord.objects.create(asset_obj=server_obj.asset, content=log_str)


    @staticmethod
    def mem_add(mem_add_list,cli_mem_data,server_obj):
        for item in mem_add_list:
            add_data = cli_mem_data[item]

            log_str = '[新增内存]插槽为{slot};容量为{capacity};类型为{model};速度为{speed};厂商为{manufacturer};SN号为{sn}'.format(
                **add_data)

            add_data['server_obj'] = server_obj
            #print('add_data',add_data)
            models.Memory.objects.create(**add_data)


            models.AssetRecord.objects.create(asset_obj=server_obj.asset, content=log_str)

    @staticmethod
    def mem_update(mem_update_list,mem_obj,server_obj,cli_mem_data):
        for item in mem_obj:
            if item.slot in mem_update_list:
                log_list = []
                new_capacity = cli_mem_data[item.slot]['capacity']
                if item.capacity != new_capacity:
                    log_list.append("[更新内存]%s:容量由%s变更为%s" %(item.slot,item.capacity, new_capacity))
                    item.capacity = new_capacity
                new_manufacturer = cli_mem_data[item.slot]['manufacturer']
                if item.manufacturer != new_manufacturer:
                    log_list.append("[更新制造厂家]%s:厂家由%s变更为%s" % (item.slot,item.manufacturer, new_manufacturer))
                    item.manufacturer = new_manufacturer

                new_model = cli_mem_data[item.slot]['model']
                if item.model != new_model:
                    log_list.append("[更新内存型号]%s:型号由%s变更为%s" % (item.slot,item.model, new_model))
                    item.model = new_model

                new_sn = cli_mem_data[item.slot]['sn']
                if item.sn != new_sn:
                    log_list.append("[更新SN]%s:SN由%s变更为%s" % (item.slot,item.sn, new_sn))
                    item.sn = new_sn

                new_speed = cli_mem_data[item.slot]['speed']
                if item.speed != new_speed:
                    log_list.append("[更新内存]%s:速度由%s变更为%s" % (item.slot,item.speed, new_speed))
                    item.speed = new_speed
                item.save()
                if log_list:
                    models.AssetRecord.objects.create(asset_obj=server_obj.asset, content=log_list)


class Disk_data(object):
    @staticmethod
    def Dis_data(server_obj,server_info):
        try:
            cli_disk = server_info['data']['Disk']
            Dis_obj = models.Disk.objects.filter(server_obj=server_obj)
            Disk_obj_list = list(map(lambda x: x, (item.slot for item in Dis_obj)))

            disk_update_list = get_in(set(Disk_obj_list), set(cli_disk.keys()))
            disk_del_list = get_exclude(Disk_obj_list, disk_update_list)
            disk_add_list = get_exclude(set(cli_disk.keys()), disk_update_list)

            Disk_data.disk_update(disk_update_list, Dis_obj, cli_disk, server_obj)
            Disk_data.disk_del(disk_del_list, Dis_obj, server_obj)
            Disk_data.disk_add(disk_add_list, cli_disk, server_obj)

        except Exception as e:
            models.ErrorLog.objects.create(asset_obj=server_obj.asset,title='错误',content="出现错误，disk测试")


    @staticmethod
    def disk_add(disk_add_list, cli_disk, server_obj):
        for item in disk_add_list:
            add_date = cli_disk[item]
            log_str = '[新增硬盘]插槽为{slot};容量为{capacity}'.format(**add_date)
            add_date['server_obj'] = server_obj
            models.Disk.objects.create(**add_date)
            models.AssetRecord.objects.create(asset_obj=server_obj.asset,content=log_str)

    @staticmethod
    def disk_del(disk_del_list, Dis_obj, server_obj):
        for item in Dis_obj:
            if item.slot in disk_del_list:
                log_str = '[删除硬盘]插槽为{slot};容量为{capacity}'.format(**item.__dict__)
                item.delete()
                models.AssetRecord.objects.create(asset_obj=server_obj.asset,content=log_str)
    @staticmethod
    def disk_update(disk_update_list, Dis_obj, cli_disk, server_obj):
        for item in Dis_obj:
            log_list = []
            if item.slot in disk_update_list:
                new_capacity = cli_disk[item.slot]['capacity']
                if item.capacity != new_capacity:
                    log_list.append("[更新硬盘]插槽为%s:容量由%s变更为%s" % (item.slot, item.capacity, new_capacity))
                    item.capacity = new_capacity
                item.save()
                if log_list:
                    models.AssetRecord.objects.create(asset_obj=server_obj.asset,content=log_list)




