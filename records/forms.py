# -*- coding: utf-8 -*-
from django import forms
from corporation.models import AppointmentHourModel,ReservedHourModel,CorpServiceModel,CorpLocModel,CorporationModel
from datetime import datetime,timedelta
from .models import AppointmentModel,RatingModel
from individual.models import IndividualModel



class AppointmentForm(forms.Form):
    corp_loc_id=forms.ModelChoiceField(queryset=CorpLocModel.objects.all())
    app_hour=forms.ModelChoiceField(queryset=AppointmentHourModel.objects.all())
    service=forms.ModelChoiceField(queryset=CorpServiceModel.objects.all())
    detail=forms.CharField(max_length=200)

    class Meta:
        fields=['corp_loc_id','app_hour','service','detail']


    def add(self,request):
        app_hour=self.cleaned_data.get('app_hour')
        service=self.cleaned_data.get('service')
        detail=self.cleaned_data.get('detail')
        res_hour=ReservedHourModel(corp_loc_id=app_hour.corp_loc_id,date=app_hour.date,start_time=app_hour.start_time,end_time=app_hour.end_time)
        res_hour.save()
        app_hour.delete()
        hop = AppointmentModel(person_id=request.user.individual_id, res_hour_id_id=res_hour.id, service=service, detail=detail)
        hop.save()

class iRatingForm(forms.ModelForm):
    corp_id = forms.ModelChoiceField(CorporationModel.objects.all())
    ind_id = forms.ModelChoiceField(IndividualModel.objects.all(),required=False,widget=forms.HiddenInput)
    value = forms.CharField(max_length=5)
    details=forms.CharField(max_length=200,required=False)

    class Meta:
        model=RatingModel
        fields=['corp_id',
                'ind_id',
                'value',
                'details']

    def add(self,request):
        print(self.clean())
        ind_id = request.user.individual_id
        corp_id = self.cleaned_data.get('corp_id')
        value = self.cleaned_data.get('value')
        detail = self.cleaned_data.get('details')

        hop = RatingModel(ind_id=ind_id,corp_id=corp_id,value=value,details=detail)
        hop.save()


class cRatingForm(forms.ModelForm):
    corp_id = forms.ModelChoiceField(CorporationModel.objects.all(), required=False,widget=forms.HiddenInput)
    ind_id = forms.ModelChoiceField(IndividualModel.objects.all())
    value = forms.CharField(max_length=5)
    details=forms.CharField(max_length=200,required=False)

    class Meta:
        model=RatingModel
        fields=['corp_id',
                'ind_id',
                'value',
                'details']

    def add(self, request):
        ind_id = self.cleaned_data.get('ind_id')
        corp_id = request.user.corporation_id
        value = self.cleaned_data.get('value')
        detail = self.cleaned_data.get('details')

        hop = RatingModel(ind_id=ind_id, corp_id=corp_id, value=value, details=detail)
        hop.save()