# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render,redirect
from .models import DistrictModel,ProvinceModel,StreetModel,TownModel,ServiceModel
from .forms import LoginForm,ServiceForm
from django.contrib.auth import(authenticate,login,logout)
from django.contrib import messages
from user.models import User

def home_page(request):
    return render(request,'home.html',{'user':request.user})


def log_in(request):
    if request.user.__str__()=='AnonymousUser':
        formuser = LoginForm()
        if request.method=='POST':
            formuser=LoginForm(request.POST)
            if formuser.is_valid():
                email = formuser.cleaned_data.get("email")
                password = formuser.cleaned_data.get("password")
                user=User.objects.get(email=email)
                user = authenticate(username=user.username,password=password)
                login(request, user)
                return redirect('http://tlhclk.pythonanywhere.com/')
        return render(request,'user/login.html',{'form':formuser})
    else:
        return redirect('http://tlhclk.pythonanywhere.com/')

def log_out(request):
    logout(request)
    return redirect('http://tlhclk.pythonanywhere.com/')

#
# def province_list(request,province_id):
#     provinces=ProvinceModel.objects.all()
#     return render(request,'main/province_list.html',{'title':'Province List','list1':provinces})
#
# def town_list(request,town_id):
#     towns=TownModel.objects.all()
#     return render(request,'main/town_list.html',{'title':'Town List','list1':towns})
#
# def district_list(request,district_id):
#     districts=DistrictModel.objects.all()
#     return render(request,'main/district_list.html',{'title':'District List','list1':districts})

def street_list(request,street_id):
    streets=StreetModel.objects.all()
    return render(request,'main/street_list.html',{'title':'Street List','list1':streets})

def service_add(request,service_id):
    if request.user.is_superuser:
        form1=ServiceForm()
        if request.POST:
            form1=ServiceForm(request.POST)
            if form1.is_valid():
                form1.save()
        return render(request,'form.html',{'form':form1})
    else:
        return redirect('http://tlhclk.pythonanywhere.com/')

def service_list(request,service_id):
    if request.user.__str__()!='AnonymousUser':
        services=ServiceModel.objects.all()
        return render(request,'main/service_list.html',{'title':'Service List','list1':services,'item_link':'http://tlhclk.pythonanywhere.com/main/service_add/','item_title':'New Service'})
    else:
        return redirect('http://tlhclk.pythonanywhere.com/')



