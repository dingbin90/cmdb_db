from django.shortcuts import render,HttpResponse,redirect
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from django.views import View
from cmdb import models
import json
from cmdb.pagina.pagernation import Pagina
import re
# Create your views here.

def index(request):
    permission_list = request.session['permission_list']
    path = request.path_info
    flag = False
    for i in permission_list:
        i = "^%s$"%i
        ret = re.match(i,path)
        if ret:
            flag = True
            break
    if not flag:
        return HttpResponse("没有权限")    
    return render(request, 'index.html')


def Assetdetail(request, id):
    # print(id)
    Asset_obj = models.Asset.objects.filter(id=id)[0]
    # print('------>',Asset_obj)
    ser_obj = Asset_obj.server
    return render(request, 'aseet_detail.html', {'Asset_obj': Asset_obj,
                                                 'ser_obj': ser_obj,
                                                 })


class AssetView(View):
    def get(self, request, *args, **kwargs):
        print(111112222)
        # asset_obj = models.Asset.objects.all()
        # pageinator = Paginator(asset_obj,2)
        #
        #
        #
        # try:
        #     contacts = pageinator.page(page)
        # except PageNotAnInteger:
        #     # If page is not an integer, deliver first page.
        #     contacts = pageinator.page(1)
        # except EmptyPage:
        #     # If page is out of range (e.g. 9999), deliver last page of results.
        #     contacts = pageinator.page(pageinator.num_pages)
        return render(request, "asset.html")


class AssetJsonView(View):
    def get(self, request, *args, **kwargs):
        pager_num = request.GET.get('page')
        if pager_num == '«':
            pass
        elif pager_num == "下一页":
            pass
        else:
            pager_num = int(request.GET.get('page'))
        #print(type(pager_num))
        # pager = json.loads(str(pager,encoding='utf-8'))
        # print(pager)
        table_config = [
            {
                'q': None,
                'title': "选项",
                'display': True,
                'text': {'content': "<input type='checkbox'/>", "kwargs": {}},
                'attrs': {}
            },
            {
                'q': "id",
                'title': "ID",
                'display': False,
                'text': {},
                'attrs': {},
            },
            {
                'q': "cabinet_num",
                'title': "机柜号",
                'display': True,
                'text': {"content": "{n}", "kwargs": {"n": "@cabinet_num"}},
                'attrs': {'name': 'cabinet_num', 'origin': '@cabinet_num', 'edit-enable': 'true', 'edit-type': 'input'}
            },
            {
                'q': "idc_id",
                'title': "IDC机房",
                'display': False,
                'text': {},
                'attrs': {}
            },
            {
                'q': "idc__name",
                'title': "IDC机房",
                'display': True,
                'text': {'content': "{n}", "kwargs": {"n": "@idc__name"}},
                'attrs': {'name': 'idc_id', 'origin': '@idc_id', 'edit-enable': 'true', 'edit-type': 'select',
                          'global-name': 'idc_choices'}
            },
            #
            # {
            #     'q': "device_type_id",
            #     'title': "资产类型",
            #     'display': True,
            #     'text': {'content': "{n}", "kwargs": {"n": "@@device_type_choices"}},
            #     'attrs': {'name':'device_type_id','origin':'@device_type_id','edit-enable': 'true', 'edit-type': 'select','global-name':'device_type_choices'}
            # },
            {
                'q': "device_status_id",
                'title': "状态",
                'display': True,
                'text': {'content': "{n}", "kwargs": {"n": "@@device_status_choices"}},
                'attrs': {'name': 'device_status_id', 'origin': '@device_status_id', 'edit-enable': 'true',
                          'edit-type': 'select', 'global-name': 'device_status_choices'}
            },
            {
                'q': None,
                'title': "操作",
                'display': True,
                'text': {
                    'content': "<div class='label label-table label-info'><a href='/cmdb/asset/detail/{m}'>{n}</a></div>",
                    "kwargs": {"n": "查看详细", "m": "@id"}},
                'attrs': {}
            },
        ]

        q_list = []
        for i in table_config:
            if not i['q']:
                continue
            q_list.append(i['q'])

        print('q_list',q_list)
        data = models.Asset.objects.all().values(*q_list)
        total_count = data.count()

        Pagnation = Pagina(total_count, pager_num)
        data = list(data)
        data = data[Pagnation.start:Pagnation.end]
        print('>>>>>>>>>>>>>>>>>>>>',data)
        result = {
            'table_config': table_config,
            'data': data,
            'global_dict': {
                'device_type_choices': models.Asset.device_type_choices,
                'device_status_choices': models.Asset.device_status_choices,
                'idc_choices': list(models.IDC.objects.values_list('id', 'name')),

            },
            'pager': Pagnation.page_str(),

        }

        return HttpResponse(json.dumps(result))

    def put(self, request, *args, **kwargs):  # 修改数据
        content = request.body
        content = json.loads(str(content, encoding='utf-8'))

        for item in content:
            # print(item)
            nid = item.pop('id')  # 获取当前得id，就是Asset得id，此id是配置文件传到前端得
            models.Asset.objects.filter(id=nid).update(**item)  # 更新数据
        ret = {
            'status': True
        }

        return HttpResponse(json.dumps(ret))

    def delete(self, request, *args, **kwargs):
        del_content = request.body
        del_content = json.loads(str(del_content, encoding='utf-8'))
        # print(del_content)
        ret = {'error': "选中选项"}
        for id in del_content:
            try:
                models.Asset.objects.filter(id=id).delete()
                # print(id)
                ret = {
                    'status': True
                }
            except Exception as e:
                ret = {
                    'error': "删除失败"
                }
        return HttpResponse(json.dumps(ret))


class ServerView(View):
    def get(self, request, *args, **kwargs):
        obj = models.Asset.objects.all().values('id', 'idc__name', 'cabinet_num', 'cabinet_order')
        obj = list(obj)
        print(obj)
        asseet_option = {}
        for item in obj:
            # print(item)
            aseet_id = item.pop('id')
            asset_op = '-'.join(item.values())
            asseet_option[aseet_id] = asset_op
        # print(asseet_option)
        return render(request, 'server-host.html', {'asseet_option': asseet_option})


class ServerJsonView(View):
    def get(self, request, *args, **kwargs):
        table_config = [
            {
                'q': None,
                'title': "选项",
                'display': True,
                'text': {'content': "<input type='checkbox'/>", "kwargs": {}},
                'attrs': {}
            },
            {
                'q': "id",
                'title': "ID",
                'display': False,
                'text': {},
                'attrs': {},
            },
            {
                'q': 'hostname',
                'title': "主机名",
                'display': True,
                'text': {'content': '{n}', "kwargs": {"n": "@hostname"}},
                'attrs': {}
            },
            {
                'q': "sn",
                'title': "SN号",
                'display': True,
                'text': {'content': "{n}", "kwargs": {"n": "@sn"}},
                'attrs': {},
            },
            {
                'q': "manage_ip",
                'title': "管理IP",
                'display': True,
                'text': {'content': "{n}", "kwargs": {"n": "@manage_ip"}},
                'attrs': {},
            },
            {
                'q': "os_platform",
                'title': "系统版本",
                'display': True,
                'text': {'content': "{n}", "kwargs": {"n": "@os_platform"}},
                'attrs': {},
            },
            {
                'q': "cpu_model",
                'title': "cpu型号",
                'display': True,
                'text': {'content': "{n}", "kwargs": {"n": "@cpu_model"}},
                'attrs': {},
            },
            {
                'q': "cpu_count",
                'title': "cpu个数",
                'display': True,
                'text': {'content': "{n}", "kwargs": {"n": "@cpu_count"}},
                'attrs': {},
            },
            {
                'q': "asset__idc__name",
                'title': "资产",
                'display': True,
                'text': {'content': "{n}", "kwargs": {"n": "@asset__idc__name"}},
                'attrs': {},
            },
        ]
        q_list = []
        for i in table_config:
            if not i['q']:
                continue
            q_list.append(i['q'])

        data = models.Server.objects.all().values(*q_list)
        data = list(data)
        print('-----',data)

        result = {
            'table_config': table_config,
            'data': data,
        }
        return HttpResponse(json.dumps(result))

    def delete(self, request, *args, **kwargs):
        del_content = request.body
        del_content = json.loads(str(del_content, encoding='utf-8'))
        # print(del_content)
        ret = {'error': "选中选项"}
        for id in del_content:
            try:
                models.Server.objects.filter(id=id).delete()
                ret = {
                    'status': True
                }
            except Exception as e:
                ret = {
                    'error': "删除失败"
                }
        return HttpResponse(json.dumps(ret))


def serverhost(request):
    if request.method == "POST":
        host_data = request.POST.copy()  # 复制一份post数据，不然数据是不可以更改得

        host_data['asset_id'] = str(host_data['asset'])
        host_data.pop('asset')

        data = {}
        for k, v in host_data.items():
            # print(k,v,type(k),type(v))
            if not v:
                continue
            else:
                data[k] = v
        print(data)
        try:
            models.Server.objects.create(**data)
        except Exception as e:
            print("出错了")
        return redirect('/cmdb/server-host/')

    return HttpResponse(".......")


def test_t(request):
    return render(request, 'test.html')
