# -*- coding: utf-8 -*-
import xadmin

from models import Course, CourseResource, Lesson, Video

__author__ = 'Ray'
__date__ = '2017/5/15 下午7:51'


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_count', 'image', 'click_count',
                    'create_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_count', 'image', 'click_count']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_count', 'image', 'click_count',
                   'create_time']


class LessonAdmin(object):
    list_display = ['course', 'name', 'create_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'create_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'create_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson__name', 'name', 'create_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download_url', 'create_time']
    search_fields = ['course', 'name', 'download_url']
    list_filter = ['course__name', 'name', 'download_url', 'create_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
