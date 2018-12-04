# -*- coding: utf-8 -*-
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import AppointmentHourModel,CorpLocModel,CorporationModel
from individual.models import IndividualModel
from datetime import datetime,timedelta,time


class AppHoourForm(forms.Form):
    start_time=forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'datetime-input'}),label='Start Time',)
    end_time=forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'datetime-input'}),label='End Time')
    amount=forms.CharField(max_length=3,label='Amount of Appointment(min)')

    class Meta:
        fields=['start_time','end_time','amount']

    def add(self,request):
        start_time=self.cleaned_data.get('start_time')
        end_time=self.cleaned_data.get('end_time')
        amount=self.cleaned_data.get('amount')
        while end_time>start_time:
            date=datetime.date(start_time)
            AppointmentHourModel(corp_loc_id=request.user.corp_loc_id,date=date,start_time=str(timedelta(hours=start_time.hour,minutes=start_time.minute)),end_time=str(timedelta(hours=start_time.hour,minutes=start_time.minute)+timedelta(minutes=int(amount)))).save()
            start_time+=timedelta(minutes=int(amount))

class CorporationForm(forms.ModelForm):
    categories = [('1', 'Hairdresser'), ('2', 'Beauty Salon'), ('3', 'Football Pitch'), ('4', 'Nutritionist'),
                  ('5', 'Psychologist'), ('6', 'Other')]
    corp_name=forms.CharField(max_length=50)
    corp_rep=forms.ModelChoiceField(queryset=IndividualModel.objects.all(),required=False)
    corp_category=forms.ChoiceField(choices=categories)
    corp_app_freq=forms.CharField(max_length=5)
    corp_rating=forms.CharField(max_length=5)
    corp_details=forms.CharField(max_length=200,required=False)
    corp_email=forms.EmailField()
    corp_phone=PhoneNumberField()

    class Meta:
        model = CorporationModel
        fields = ['corp_name',
                  'corp_rep',
                  'corp_category',
                  'corp_app_freq',
                  'corp_rating',
                  'corp_details',
                  'corp_email',
                  'corp_phone',
                  ]
