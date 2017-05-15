# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, default='', verbose_name='昵称')
    birthday = models.DateField(null=True, blank=True, verbose_name=u'生日')
    gender = models.CharField(max_length=10, choices=(('male', '男'), ('female', '女')), default='female',
                              verbose_name='性别')
    address = models.CharField(max_length=100, default='', verbose_name='地址')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机')
    image = models.ImageField(max_length=100, upload_to='image/%Y/%m', default='image/default.png',
                              verbose_name='用户头像')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='注册时间')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=10, verbose_name='验证码')
    email = models.CharField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(max_length=10, choices=(('register', '注册'), ('forget', '找回密码')),
                                 verbose_name='验证码类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField(max_length=30, verbose_name='标题')
    image = models.ImageField(max_length=50, upload_to='banner/%Y/%m', verbose_name='图片地址')
    url = models.URLField(max_length=200, verbose_name='跳转地址')
    index = models.IntegerField(default=100, verbose_name='索引号')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
