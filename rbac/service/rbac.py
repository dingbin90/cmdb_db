from django.utils.deprecation import MiddlewareMixin
import re
from django.shortcuts import HttpResponse,redirect

class Validatepermisson(MiddlewareMixin):
    def process_request(self,request):
        #检查url白名单
        path = request.path_info
        white_url = ['/login','/admin/.*']
        for i in white_url:
            ret = re.match(i,path)
            if ret:
                return None


        #判断是否登陆
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('/login')




        #校验权限
        permission_list = request.session.get('permission_list',[])
        #print('asset/detail/(\d+)',permission_list)
        path = request.path_info
        flag = False
        for i in permission_list:
            i = "^%s$" % i
            ret = re.match(i, path)
            if ret:
                flag = True
                break
        if not flag:
            return HttpResponse("没有权限")
        return None