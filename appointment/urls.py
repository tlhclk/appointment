# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from main.views import home_page,log_in,log_out


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^corporation/',include('corporation.urls')),
    url(r'^individual/',include('individual.urls')),
    url(r'^main/',include('main.urls')),
    url(r'^record/',include('records.urls')),
    url(r'^user/',include('user.urls')),
    url(r'^login/$', log_in,name='login'),
    url(r'^logout/$', log_out, name='logout'),
    url(r'^$',home_page,name='home_page'),

]
