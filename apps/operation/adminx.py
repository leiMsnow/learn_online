# -*- coding: utf-8 -*-
import xadmin
from operation.models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse

__author__ = 'Ray'
__date__ = '2017/5/15 下午8:18'


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'create_time']
    list_filter = ['name', 'mobile', 'course_name', 'create_time']
    search_fields = ['name', 'mobile', 'course_name']


class CourseCommentsAdmin(object):
    list_display = ['course', 'user', 'course_name', 'comments', 'create_time']
    list_filter = ['course', 'user', 'course_name', 'comments', 'create_time']
    search_fields = ['course', 'user', 'course_name', 'comments']


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'create_time']
    list_filter = ['user', 'fav_id', 'fav_type', 'create_time']
    search_fields = ['user', 'fav_id', 'fav_type']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'create_time']
    list_filter = ['user', 'message', 'has_read', 'create_time']
    search_fields = ['user', 'message', 'has_read']


class UserCourseAdmin(object):
    list_display = ['course', 'user', 'create_time']
    list_filter = ['course', 'user', 'create_time']
    search_fields = ['course', 'user']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
