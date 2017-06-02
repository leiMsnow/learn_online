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
        hot_orgs = all_orgs.order_by('-click_count')[:3]
        # 筛选城市
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        # 筛选类别
        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category=category)

        # 排序类型
        sort = request.GET.get('sort', '')
        if sort:
            all_orgs = all_orgs.order_by('-{0}'.format(sort))
            # if sort == 'students':
            #     all_orgs = all_orgs.order_by('-students')
            # elif sort == 'courses':
            #     all_orgs = all_orgs.order_by('-courses')

        try:
            page_index = request.GET.get('page', 1)
        except PageNotAnInteger:
            page_index = 1

        p = Paginator(all_orgs, 2)
        current_org = p.page(page_index)

        org_count = all_orgs.count()

        return render(request, 'org-list.html', {
            'all_orgs': current_org,
            'all_citys': all_citys,
            'org_count': org_count,
            'city_id': city_id,
            'category': category,
            'hot_orgs': hot_orgs,
            'sort': sort,
        })

