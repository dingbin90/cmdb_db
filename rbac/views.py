from django.shortcuts import render,HttpResponse,redirect
import json

# Create your views here.
from rbac import models


# 角色
def role(request):
    role_obj = models.Role.objects.all()

    return render(request, 'rbac/role.html', {'role_obj': role_obj})


# 返回权限树所需的数据格式ztree的
def roleaddjson(request):
    url_obj = models.PermisionUrl.objects.all()
    url_data = []
    head_dic = {'id': '1', 'pId': 0, 'name': "权限列表", 'open': True}
    url_data.append(head_dic)
    for i in url_obj:
        dic = {}
        dic['id'] = str(int(i.id) + 1)
        dic['pId'] = '1'
        dic['name'] = i.title + i.url
        url_data.append(dic)

    # print(url_data)
    return HttpResponse(json.dumps(url_data))


# 权限授权
def addaccess(request):
    if request.method == "POST":
        url_list = json.loads(request.POST.get('node_id'))
        roleid = request.POST.get("roleid")
        del url_list[-1]
        role_obj = models.Role.objects.get(id=roleid)
        role_obj.permissonurl.set(url_list)

        return HttpResponse(json.dumps(u'授权成功'))


# 角色添加
def roleadd(request):
    if request.method == "POST":
        title = request.POST.get('title')
        mem = request.POST.get('mem')
        title_obj = models.Role.objects.all().values('title')
        title_lsit = []
        for i in title_obj:
            title_lsit.append(i['title'])
        try:
            if not title in title_lsit:
                models.Role.objects.create(title=title, mom=mem)
            else:
                print('角色已经存在')
        except Exception as e:
            print()

        return redirect('/rbac/role/')
    return render(request, 'rbac/roleadd.html')


# 权限
def access(request):
    access_obj = models.PermisionUrl.objects.all()

    return render(request, 'rbac/access-list.html', {'access_obj': access_obj})


# 权限添加
def accessadd(request):
    if request.method == "POST":
        list_data = request.POST
        # print(list_data)
        try:
            models.PermisionUrl.objects.create(**list_data)
            return redirect('/rbac/access-list/')
        except Exception as e:
            print('出错了')
    return HttpResponse(".........")


# 权限删除
def accdelete(request, id):
    acc_obj = models.PermisionUrl.objects.get(id=id)
    if request.method == "POST":
        models.PermisionUrl.objects.get(id=id).delete()
        return redirect('/rbac/access-list/')
    return render(request, 'rbac/accdelete.html', {"acc_obj": acc_obj})


# 测试
def test(request):
    return render(request, 'tete.html')


# 登陆
def acc_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = models.User.objects.filter(name=username, pwd=password).first()

        if user:
            request.session['user_id'] = user.id
            permission = user.role.all().values('permissonurl__url')
            # print(permission)
            permission_list = []
            for item in permission:
                permission_list.append(item['permissonurl__url'])
            # print(permission_list)
            request.session['permission_list'] = permission_list
            return redirect("/cmdb/index")
    return render(request, 'login.html')



#账户信息
def account(request):
    acc_obj = models.User.objects.all()


    return render(request,'rbac/account.html',{'acc_obj':acc_obj})


def accountadd(request):
    role_obj = models.Role.objects.all()
    user_obj = models.User.objects.all().values('name')
    user_list = []
    for i in user_obj:
        user_list.append(i['name'])
    msg = {}
    if request.method == "POST":
        try:
            name = request.POST.get('name')
            password = request.POST.get('pwd')
            role_list = request.POST.get('role')
            if name in user_list:
                msg['error'] = u"用户已存在"
            else:
                models.User.objects.create(name=name,pwd=password)
                models.User.objects.get(name=name).role.set(role_list)
                return redirect('/rbac/account')
        except Exception as e:
            print(e)
        return render(request,'rbac/accountadd.html',{'role_obj':role_obj,'msg':msg})
    return render(request,'rbac/accountadd.html',{'role_obj':role_obj})


def accountdelete(request,id):
    account_obj = models.User.objects.get(id=id)
    if request.method == "POST":
        account_obj.delete()
        return redirect('/rbac/account')
    return render(request,'rbac/accountdelete.html',{'account_obj':account_obj})
