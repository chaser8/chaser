#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/6/11 3:08 下午
# @Author : yangzb
# @Site : https://www.yangzb.com
# @File : urls.py
# @Software: PyCharm
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]