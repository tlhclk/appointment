# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from .views import user_list,user_detail

app_name='user'
urlpatterns = [
    url(r'^user_list/(?P<user_id>[0-9]*)$',user_list,name='user_list'),
    url(r'^user_detail/(?P<user_id>[0-9]*)$',user_detail,name='user_detail'),
    ]