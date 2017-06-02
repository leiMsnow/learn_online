# -*- coding: utf-8 -*-
from django.conf.urls import url

from operation.views import AddUserAskView
from organization.views import OrgView

__author__ = 'Ray'
__date__ = '2017/6/2 下午12:59'

urlpatterns = [

    # 课程相关
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask'),
]
