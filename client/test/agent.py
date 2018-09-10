# import  subprocess
# import requests
#
# ######采集数据###########33
# result = subprocess.getoutput('ifconfig')
# #处理result的数据
#
# #整理data数据
#
# date_dic = {
#    'nic':{},
#     'disk':{},
#     'mem':{}
# }
#
# ########发送数据#####################33
# #发送数据
# requests.post('http://127.0.0.1/asset.html',data=date_dic)
import platform

print(platform.system())