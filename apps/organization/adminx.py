# -*- coding: utf-8 -*-
import xadmin
from .models import CityDict, CourseOrg, Teacher

__author__ = 'Ray'
__date__ = '2017/5/15 下午8:13'


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'code', 'create_time']
    list_filter = ['name', 'desc', 'code', 'create_time']
    search_fields = ['name', 'desc', 'code']


class CourseOrgAdmin(object):
    list_display = ['city', 'name', 'desc', 'click_count', 'fav_count', 'image', 'address', 'create_time']
    list_filter = ['city', 'name', 'desc', 'click_count', 'fav_count', 'image', 'address', 'create_time']
    search_fields = ['city', 'name', 'desc', 'click_count', 'fav_count', 'image', 'address']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_count', 'fav_count',
                    'image', 'create_time']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_count', 'fav_count',
                   'image', 'create_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_count', 'fav_count',
                     'image']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
