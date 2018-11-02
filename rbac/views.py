from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from rbac import models


def role(request):
    role_obj = models.Role.objects.all()
    return render(request,'rbac/role.html',{'role_obj':role_obj})


def access(request):

    access_obj = models.PermisionUrl.objects.all()

    return  render(request,'rbac/access-list.html',{'access_obj':access_obj})

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

def accdelete(request,id):
    acc_obj = models.PermisionUrl.objects.get(id=id)
    if request.method == "POST":
        models.PermisionUrl.objects.get(id=id).delete()
        return redirect('/rbac/access-list/')
    return render(request,'rbac/accdelete.html',{"acc_obj":acc_obj})



def test(request):
    return render(request,'tete.html')


def acc_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = models.User.objects.filter(name=username,pwd=password).first()

        if user:
            request.session['user_id'] = user.id
            permission = user.role.all().values('permissonurl__url')
            #print(permission)
            permission_list = []
            for item in permission:
                permission_list.append(item['permissonurl__url'])
            #print(permission_list)
            request.session['permission_list'] = permission_list
            return redirect("/cmdb/index")
    return render(request,'login.html')
