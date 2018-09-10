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
from cmdb import views

urlpatterns = [
    re_path('^index/$',views.index,name='index-zy'),
    re_path('^asset/$',views.AssetView.as_view(),name='cmdb-aseet'),
    re_path('^asset/detail/(\d+)',views.Assetdetail),
    re_path('^asset-json/$',views.AssetJsonView.as_view()),
    re_path('^server-host/$',views.ServerView.as_view(),name='server-host'),
    re_path('^server-host/add/$',views.serverhost),
    re_path('^server-host-json/$',views.ServerJsonView.as_view()),
    re_path('^test/$',views.test_t),

]
