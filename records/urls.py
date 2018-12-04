# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import appointment_list,find_available_appointments,make_appointment,busy_day,show_close_corp,\
    most_popular_service,rating_list,rate,most_appointer,busy_hour,complain

app_name='record'
urlpatterns = [
    url(r'^appointment_list/(?P<appointment_id>[0-9]*)$',appointment_list,name='appointment_list'),
    url(r'^faa/$',find_available_appointments,name='faa'),
    url(r'^make_appointment/$',make_appointment,name='make_appointment'),
    url(r'^busy_day/(?P<m_l>(m|l)*)$',busy_day,name='busy_day'),
    url(r'^most_popular_service/(?P<date>([0-9]*-*[0-9]*w*))$',most_popular_service,name='most_popular_service'),
    url(r'^show_close_corp/(?P<degree>(p|t|d|s)*)$',show_close_corp,name='show_close_corp'),
    url(r'^rating_list/(?P<rating_id>[0-9]*)$',rating_list,name='rating_list'),
    url(r'^rate/(?P<i_c>(i|c)*)$',rate,name='rate'),
    url(r'^most_appointer/(?P<id>[0-9]*)$',most_appointer,name='most_appointer'),
    url(r'^busy_hour/(?P<time>[0-9]*)$',busy_hour,name='busy_hour'),
    url(r'^complain/(?P<id>[0-9]*)$',complain,name='complain'),
    ]