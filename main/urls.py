# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import province_list,town_list,district_list,street_list,service_list,service_add

app_name='main'
urlpatterns = [
    url(r'^province_list/(?P<province_id>[0-9]*)$',province_list,name='province_list'),
    url(r'^town_list/(?P<town_id>[0-9]*)$',town_list,name='town_list'),
    url(r'^district_list/(?P<district_id>[0-9]*)$',district_list,name='district_list'),
    url(r'^street_list/(?P<street_id>[0-9]*)$',street_list,name='street_list'),
    url(r'^service_list/(?P<service_id>[0-9]*)$',service_list,name='service_list'),
    url(r'^service_add/(?P<service_id>[0-9]*)$',service_add,name='service_add'),
    ]