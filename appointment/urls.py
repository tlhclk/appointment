# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from django.contrib import admin
from main.views import home_page,log_in,log_out
from django.conf.urls import (handler400, handler403, handler404, handler500)


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

handler404 = 'main.views.handler404'
handler500 = 'main.views.handler500'
handler400 = 'main.views.handler400'
handler403 = 'main.views.handler403'