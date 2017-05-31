# -*- coding: utf-8 -*-
import xadmin
from xadmin import views

from models import EmailVerifyRecord, Banner

__author__ = 'Ray'
__date__ = '2017/5/15 下午7:14'


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class CommSettings(object):
    site_title = 'Learn学院后台管理系统'
    site_footer = 'Learn学院在线'
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_time', 'send_type']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_time', 'send_type']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'create_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'create_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, CommSettings)
