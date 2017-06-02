# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.views.generic import View

from users.forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm
from users.models import UserProfile, EmailVerifyRecord
from utils.emil_send import send_register_email


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as err:
            print("error: %s", err)
            return None


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
            if UserProfile.objects.filter(email=user_name):
                return render(request, 'register.html', {'msg': '用户已经存在！', 'register_form': register_form})
            else:
                pass_word = request.POST.get('password', '')
                user = UserProfile()
                user.username = user_name
                user.email = user_name
                user.is_active = False
                user.password = make_password(pass_word)
                user.save()

                send_register_email(user_name, 'register')
                return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'register_form': register_form})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html', {'user': user})
                else:
                    return render(request, 'login.html', {'msg': '用户尚未激活！', 'login_form': login_form})
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误！', 'login_form': login_form})
        else:
            return render(request, 'login.html', {'login_form': login_form})


class ActiveView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, 'active_fail.html')
        return render(request, 'login.html')


class ForgetView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, 'forget_pwd.html', {'forget_form': forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email', '')
            if UserProfile.objects.filter(email=email):
                send_register_email(email=email, send_type='forget')
                return render(request, 'send_success.html')
            else:
                return render(request, 'forget_pwd.html', {'msg': '账号不存在！', 'forget_form': forget_form})
        else:
            return render(request, 'forget_pwd.html', {'forget_form': forget_form})


class ResetView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, 'password_reset.html', {'email': email, 'active_code': active_code})
        else:
            return render(request, 'active_fail.html', {'msg': '连接已经失效！'})


class ModifyPwdView(View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        email = request.POST.get('email', '')
        active_code = request.POST.get('active_code', '')

        codes = EmailVerifyRecord.objects.get(code=active_code)
        if codes is None:
            return render(request, 'active_fail.html', {'msg': '修改密码连接已经失效！'})

        if modify_form.is_valid():
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            if pwd1 != pwd2:
                return render(request, 'password_reset.html', {'email': email, 'active_code': active_code,
                                                               'msg': '密码不一致！'})
            user = UserProfile.objects.get(email=email)
            if user:
                user.password = make_password(pwd1)
                user.save()

                codes.delete()
                return render(request, 'login.html')
        else:
            return render(request, 'password_reset.html', {'email': email, 'active_code': active_code,
                                                           'modify_form': modify_form})
