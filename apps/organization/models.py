# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name='城市名称')
    desc = models.CharField(max_length=200, verbose_name='城市描述')
    code = models.IntegerField(verbose_name='城市编号')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '城市信息'
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    city = models.ForeignKey(CityDict, verbose_name='所在城市')
    name = models.CharField(max_length=50, verbose_name='机构名称')
    desc = models.CharField(max_length=500, verbose_name='机构描述')
    click_count = models.IntegerField(default=0, verbose_name='点击数量')
    fav_count = models.IntegerField(default=0, verbose_name='收藏数量')
    image = models.ImageField(max_length=100, upload_to='org/%Y/%m', verbose_name='机构封面')
    address = models.CharField(max_length=150, verbose_name='机构地址')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '机构信息'
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name='所属机构')
    name = models.CharField(max_length=50, verbose_name='教师名称')
    work_years = models.IntegerField(default=0, verbose_name='工作年限')
    work_company = models.CharField(max_length=100, verbose_name='就职公司')
    work_position = models.CharField(max_length=100, verbose_name='公司职位')
    points = models.CharField(max_length=100, verbose_name='教学特点')
    click_count = models.IntegerField(default=0, verbose_name='点击数量')
    fav_count = models.IntegerField(default=0, verbose_name='收藏数量')
    image = models.ImageField(max_length=100, upload_to='teacher/%Y/%m', verbose_name='教师头像')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '教师信息'
        verbose_name_plural = verbose_name

