# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User,Group,Permission,ContentType
from django.contrib.auth import (authenticate, get_user_model, password_validation,login)
from django.contrib.auth import get_user_model
from .models import ServiceModel


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email Adresi', widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput)


class ServiceForm(forms.ModelForm):
    service_title=forms.CharField(max_length=50)
    service_detail=forms.CharField(max_length=200)

    class Meta:
        model=ServiceModel
        fields=['service_title',
                'service_detail']
