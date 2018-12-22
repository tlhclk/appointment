# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from .models import CorporationModel,CorpLocModel,AppointmentHourModel,CorpServiceModel
from .forms import AppHourForm,CorporationForm,CorpLocForm
from django.contrib.auth.base_user import make_password
from django.utils.timezone import now
from user.views import user_add
from datetime import datetime,timedelta


def corporation_list(request,corporation_id):
    if request.user.__str__()!='AnonymousUser':
        corporations=CorporationModel.objects.all()
        return render(request, 'corp/corporation_list.html', {'title': 'Corporation List', 'list1': corporations,
                                                     'item_link': 'http://eceuslu.pythonanywhere.com/corporation/corporation_add/',
                                                     'item_title': 'New Corporation'})
    else:
        return redirect('http://eceuslu.pythonanywhere.com/')


def corporation_add(request,corporation_id):
    if request.user.__str__()=='AnonymousUser':
        form1=CorporationForm()
        if request.POST:
            form1=CorporationForm(request.POST)
            if form1.is_valid():
                form1.save()
                user_dict={'password':make_password('426936'),
                          'is_superuser':False,
                          'username':request.POST['corp_email'].split('@')[0],
                          'first_name':request.POST['corp_name'],
                          'last_name':'',
                          'email':request.POST['corp_email'],
                          'is_staff':True,
                          'is_active':True,
                          'date_joined':now(),
                          'corporation_id':CorporationModel.objects.all().last()
                          }
                user_add(user_dict)
        return render(request,'corp/corporation_add.html',{'form':form1,'title':'New Corporation'})
    else:
        return redirect('http://eceuslu.pythonanywhere.com/')


def corp_loc_list(request,corp_loc_id):
    if request.user.__str__()!='AnonymousUser':
        if request.user.corporation_id!=None:
            corp_locs=CorpLocModel.objects.filter(corporation=request.user.corporation_id)
            return render(request,'corp/corp_loc_list.html',{'title':'Corporation Locations List','list1':corp_locs,
                                                             'item_link':'http://eceuslu.pythonanywhere.com/corporation/corp_loc_add/',
                                                             'item_title':'New Corporation Location'})
    else:
        return redirect('http://eceuslu.pythonanywhere.com/')


def app_hour_list(request,app_hour_id):
    if request.user.__str__()!='AnonymousUser':
        if request.user.corporation_id!=None:
            app_hours=AppointmentHourModel.objects.filter(corp_loc_id__corporation=request.user.corporation_id)
            return render(request,'corp/app_hour_list.html',{'title':'Appointment Hour List','list1':app_hours,'item_link':'http://eceuslu.pythonanywhere.com/corporation/app_hour_add/','item_title':'New Appoinment Hour'})
        else:
            return redirect('http://eceuslu.pythonanywhere.com/')
    else:
        return redirect('http://eceuslu.pythonanywhere.com/')


def corp_service_list(request,corp_service_id):
    if request.user.__str__()!='AnonymousUser':
        if request.user.corporation_id!=None:
            corp_services=CorpServiceModel.objects.filter(corporation_id=request.user.corporation_id)
            return render(request,'corp/corp_service_list.html',{'title':'Corporation Service List','list1':corp_services})
        else:
            return redirect('http://eceuslu.pythonanywhere.com/')
    else:
        return redirect('http://eceuslu.pythonanywhere.com/')


def app_hour_add(request,app_hour_id):
    if request.user.__str__()!='AnonymousUser':
        if request.user.corporation_id!=None:
            form1=AppHourForm(request.user)
            if request.POST:
                form1=AppHourForm(request.user,request.POST)
                if form1.is_valid():
                    form1.add(request)
            return render(request,'corp/app_hour_add.html',{'form':form1,'title':'Add New Appointment Hour'})
        return redirect('http://eceuslu.pythonanywhere.com/')
    else:
        return redirect('http://eceuslu.pythonanywhere.com/')


def corp_loc_add(request,corp_loc_id):
    if request.user.__str__()=='AnonymousUser':
        if request.user.corporation_id!=None:
            form1=CorpLocForm()
            if request.POST:
                form1=CorpLocForm(request.POST)
                if form1.is_valid():
                    form1.save()
            return render(request,'corp/corp_loc_add.html',{'form':form1,'title':'Add New Location For Corporations'})
        else:
            return redirect('http://eceuslu.pythonanywhere.com/')
    else:
        return redirect('http://eceuslu.pythonanywhere.com/')