# -*- coding: utf-8 -*-
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import IndividualModel,StreetModel


class IndividualForm(forms.ModelForm):
    status=[('1','Married'),('2','Single')]
    gender=[('1','Male'),('2','Female')]
    ind_name = forms.CharField(max_length=50)
    ind_lastname = forms.CharField(max_length=50)
    ind_email = forms.EmailField()
    ind_phone = PhoneNumberField()
    ind_detail = forms.CharField(max_length=200)
    ind_loc_id = forms.ModelChoiceField(queryset=StreetModel.objects.all(),required=False)
    ind_no = forms.CharField(max_length=11)
    ind_bday = forms.DateField()
    ind_statu = forms.ChoiceField(choices=status,widget=forms.Select(),required=False)
    ind_gender = forms.ChoiceField(choices=gender,widget=forms.Select(),required=False)

    class Meta:
        model=IndividualModel
        fields=['ind_name',
                'ind_lastname',
                'ind_email',
                'ind_phone',
                'ind_detail',
                'ind_loc_id',
                'ind_no',
                'ind_bday',
                'ind_statu',
                'ind_gender',
                ]