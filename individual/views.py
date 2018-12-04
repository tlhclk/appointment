# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from .models import IndividualModel
from .forms import IndividualForm
from django.contrib.auth.base_user import make_password
from django.utils.timezone import now
from user.views import user_add
from datetime import datetime,timedelta

def individual_list(request,individual_id):
    if request.user.__str__()!='AnonymousUser':
        individuals=IndividualModel.objects.all()
        return render(request, 'list_any.html', {'title': 'Individual List', 'list1': individuals,
                                             'item_link': 'http://tlhclk.pythonanywhere.com/individual/individual_add/',
                                             'item_title': 'New Individual'})
    else:
        return redirect('http://tlhclk.pythonanywhere.com/')

def individual_add(request,individual_id):
    if request.user.__str__()=='AnonymousUser':
        form1=IndividualForm()
        if request.POST:
            form1=IndividualForm(request.POST)
            if form1.is_valid():
                form1.save()
                user_dict={'password':make_password('426936'),
                          'is_superuser':False,
                          'username':request.POST['ind_email'].split('@')[0],
                          'first_name':request.POST['ind_name'],
                          'last_name':request.POST['ind_lastname'],
                          'email':request.POST['ind_email'],
                          'is_staff':True,
                          'is_active':True,
                          'date_joined':now(),
                          'individual_id':IndividualModel.objects.all().last()
                          }

                user_add(user_dict)
        return render(request,'form.html',{'form':form1})
    else:
        return redirect('http://tlhclk.pythonanywhere.com/')
