# -*- coding: utf-8 -*-
import random
import string

from django.core.mail import send_mail

from mx_online.settings import EMAIL_FROM
from users.models import EmailVerifyRecord

__author__ = 'Ray'
__date__ = '2017/5/17 下午3:11'


def random_str(random_length=8):
    return ''.join(random.choice(string.letters + string.digits) for i in range(random_length))


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_subject = ''
    email_message = ''

    if send_type == 'register':
        email_subject = 'Learn学院注册激活'
        email_message = '点击连接激活你的账号: http://127.0.0.1:8000/active/{0}'.format(code)
    elif send_type == 'forget':
        email_subject = 'Learn学院密码找回'
        email_message = '点击连接找回你的密码: http://127.0.0.1:8000/reset/{0}'.format(code)

    send_status = send_mail(email_subject, email_message, EMAIL_FROM, [email])
    if send_status:
        pass
