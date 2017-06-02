# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.
from django.views.generic import View
from django.http import HttpResponse

from operation.forms import UserAskForm


class AddUserAskView(View):
    def post(self, request):
        user_ask_form = UserAskForm(request.POST)
        if user_ask_form.is_valid():
            user_ask = user_ask_form.save(commit=True)
            return HttpResponse("{'status':'success'}", content_type='application/json')
        else:
            return HttpResponse("{'status':'fail', 'msg': '添加失败！'}", content_type='application/json')