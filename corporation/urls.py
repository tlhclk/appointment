# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import corporation_list,corp_loc_list,app_hour_list,corp_service_list,app_hour_add,corporation_add,corp_loc_add
from records.views import show_appointments

app_name='corporation'
urlpatterns = [
    url(r'^corporation_list/(?P<corporation_id>[0-9]*)$',corporation_list,name='corporation_list'),
    url(r'^corporation_add/(?P<corporation_id>[0-9]*)$',corporation_add,name='corporation_add'),
    url(r'^corp_loc_list/(?P<corp_loc_id>[0-9]*)$',corp_loc_list,name='corp_loc_list'),
    url(r'^app_hour_list/(?P<app_hour_id>[0-9]*)$',app_hour_list,name='app_hour_list'),
    url(r'^corp_service_list/(?P<corp_service_id>[0-9]*)$',corp_service_list,name='corp_service_list'),
    url(r'^app_hour_add/(?P<app_hour_id>[0-9]*)$',app_hour_add,name='app_hour_add'),
    url(r'^appointment_list/(?P<date>(i|c)([0-9]*-*[0-9]*w*|o|n))$',show_appointments,name='show_appointment'),
    url(r'^corp_loc_add/(?P<corp_loc_id>[0-9]*)$',corp_loc_add,name='corp_loc_add'),
    ]