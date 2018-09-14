from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from rbac import models

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
