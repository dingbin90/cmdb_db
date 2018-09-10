from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
from cmdb import models
from api.server.asset import Server_data_info,Nic_data_info,Mem_data_info,Disk_data
# Create your views here.

@csrf_exempt
def AssetViewdata(request):
    if request.method == "POST":
        server_info = json.loads(request.body,encoding='utf-8')
        hostname = server_info['hostname']
        ret = {'code': 1000, 'message': '[%s]更新完成' % hostname}
        server_obj = models.Server.objects.filter(hostname=hostname).first()
        if not server_obj:
            ret['code'] = 1002
            ret['message'] = '资产不存在'
            return HttpResponse(ret)

        else:
            server_da_obj = Server_data_info()
            server_da_obj.data_change(server_obj,server_info)
            server_da_obj.update_aseet_lasttime(server_obj)
            nic_da_obj = Nic_data_info()
            nic_da_obj.nic_data(server_obj,server_info)
            mem_da_obj = Mem_data_info()
            mem_da_obj.Mem_data(server_obj,server_info)
            dis_da_obj = Disk_data()
            dis_da_obj.Dis_data(server_obj,server_info)
            #ret['code'] = 1000
            #ret['message'] = '资产更新成功'
            return JsonResponse(ret)

    return HttpResponse('.......')

