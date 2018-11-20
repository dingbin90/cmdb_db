"""cmdb_db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from rbac import views

urlpatterns = [
    re_path('^role/$',views.role,name='role'),
    re_path('^role/add$',views.roleadd,name='roleadd'),
    re_path('^role/addjson/$',views.roleaddjson),
    re_path('^role/addaccess$',views.addaccess),
    re_path('account/$',views.account,name='account'),
    re_path('account/add$',views.accountadd,name='accountadd'),
    re_path('account/delete/(\d+)$',views.accountdelete,name='account-delete'),
    re_path('^access-list/$',views.access,name='access-list'),
    re_path('^access-list/add/$',views.accessadd),
    re_path('^access-list/delete/(\d+)$',views.accdelete,name='access-delete'),
    re_path('^test/$',views.test),  #测试url


  ]
