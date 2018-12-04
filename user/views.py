# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from .models import User


def user_list(request,user_id):
    if request.user.__str__()!='AnonymousUser':
        if request.user.is_superuser:
            user=User.objects.all()
            return render(request,'list_any.html',{'title':'User List','list1':user})
    else:
        return redirect('http://tlhclk.pythonanywhere.com/')


def user_add(user_dict):
    if 'individual_id' in user_dict:
        new_user=User(password=user_dict['password'],
            is_superuser=user_dict['is_superuser'],
            username=user_dict['username'],
            first_name=user_dict['first_name'],
            last_name=user_dict['last_name'],
            email=user_dict['email'],
            is_staff=user_dict['is_staff'],
            is_active=user_dict['is_active'],
            date_joined=user_dict['date_joined'],
            individual_id=user_dict['individual_id'],)
    else:
        new_user=User(password=user_dict['password'],
            is_superuser=user_dict['is_superuser'],
            username=user_dict['username'],
            first_name=user_dict['first_name'],
            last_name=user_dict['last_name'],
            email=user_dict['email'],
            is_staff=user_dict['is_staff'],
            is_active=user_dict['is_active'],
            date_joined=user_dict['date_joined'],
            corporation_id=user_dict['corporation_id'],)
    new_user.save()


def user_detail(request,user_id):
    user=User.objects.get(pk=user_id)
    return render(request,'user_detail.html',{'user':user,
                                              'title':'User Details:'+user.last_name+', '+user.first_name})