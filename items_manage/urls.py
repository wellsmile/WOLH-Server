#coding=utf-8
'''
Created on 2018年6月19日

@author: xiaochengcao
'''
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^WOLH/items/$', views.items_data, name='items_data'),
]