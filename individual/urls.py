# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import individual_list,individual_add
from records.views import show_appointments

app_name='individual'
urlpatterns = [
    url(r'^individual_list/(?P<individual_id>[0-9]*)$',individual_list,name='individual_list'),
    url(r'^individual_add/(?P<individual_id>[0-9]*)$',individual_add,name='individual_add'),
    url(r'^appointment_list/(?P<date>(i|c)([0-9]*-*[0-9]*w*|o|n))$',show_appointments,name='show_appointment'),
    ]