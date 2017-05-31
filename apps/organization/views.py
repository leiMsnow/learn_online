# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pure_pagination import PageNotAnInteger, Paginator
from django.shortcuts import render
from django.views.generic import View

from .models import CourseOrg, CityDict


class OrgView(View):
    def get(self, request):

        all_orgs = CourseOrg.objects.all()
        all_citys = CityDict.objects.all()
        org_count = all_orgs.count()

        try:
            page_index = request.GET.get('page', 1)
        except PageNotAnInteger:
            page_index = 1

        p = Paginator(all_orgs, 2)
        current_org = p.page(page_index)

        return render(request, 'org-list.html', {
            'all_orgs': current_org,
            'all_citys': all_citys,
            'org_count': org_count,
        })
