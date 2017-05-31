# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='课程名称')
    desc = models.CharField(max_length=300, verbose_name='课程描述')
    detail = models.TextField(verbose_name='课程详情')
    degree = models.CharField(max_length=10, choices=(('cj', '初级'), ('zj', '中级'), ('gj', '高级')),
                              verbose_name='课程等级')
    learn_times = models.IntegerField(default=0, verbose_name='课程时长（分钟）')
    students = models.IntegerField(default=0, verbose_name='学习人数')
    fav_count = models.IntegerField(default=0, verbose_name='收藏人数')
    image = models.ImageField(max_length=100, upload_to='course/%Y/%m', verbose_name='课程封面')
    click_count = models.IntegerField(default=0, verbose_name='课程点击数')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='章节名称')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '章节信息'
        verbose_name_plural = verbose_name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name='章节')
    name = models.CharField(max_length=100, verbose_name='视频名称')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '视频信息'
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='资源名称')
    download_url = models.FileField(max_length=200, upload_to='course/resource/%Y/%m', verbose_name='资源地址')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '资源信息'
        verbose_name_plural = verbose_name
