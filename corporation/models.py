# -*- coding: utf-8 -*-
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from main.models import StreetModel,ServiceModel
from individual.models import IndividualModel
from datetime import date


class CorporationModel(models.Model):
    categories=[('1','Hairdresser'),('2','Beauty Salon'),('3','Football Pitch'),('4','Nutritionist'),('5','Psychologist'),('6','Other')]
    corp_name=models.CharField(max_length=50)
    corp_rep=models.ForeignKey(IndividualModel,on_delete=models.CASCADE,null=True)
    corp_category=models.CharField(max_length=50,choices=categories)
    corp_app_freq=models.CharField(max_length=5)
    corp_rating=models.CharField(max_length=5)
    corp_details=models.CharField(max_length=200,null=True,blank=True)
    corp_email=models.EmailField()
    corp_phone=PhoneNumberField(default='+905554443322')

    class Meta:
        db_table='corporation_table'

    def __str__(self):
        return str(self.corp_name)


class CorpLocModel(models.Model):
    corporation=models.ForeignKey(CorporationModel,on_delete=models.CASCADE)
    location=models.ForeignKey(StreetModel,on_delete=models.CASCADE)

    class Meta:
        db_table='corp_loc_table'

    def __str__(self):
        return str(self.corporation.corp_name)+' - '+str(self.location)


class AppointmentHourModel(models.Model):
    corp_loc_id=models.ForeignKey(CorpLocModel,on_delete=models.CASCADE)
    date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()

    class Meta:
        db_table='appointment_hour_table'

    def __str__(self):
        return str(self.corp_loc_id)+' - '+str(self.date)+' - '+str(self.start_time)+' - '+str(self.end_time)



class CorpServiceModel(models.Model):
    corp_loc_id=models.ForeignKey(CorpLocModel,on_delete=models.CASCADE)
    service_id=models.ForeignKey(ServiceModel,on_delete=models.CASCADE)
    details=models.CharField(max_length=200,null=True,blank=True)

    class Meta:
        db_table='corp_service_table'

    def __str__(self):
        return str(self.corp_loc_id)+' - '+str(self.service_id)


class ReservedHourModel(models.Model):
    corp_loc_id=models.ForeignKey(CorpLocModel,on_delete=models.CASCADE)
    date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()

    class Meta:
        db_table='reserved_hour_table'

    def __str__(self):
        return str(self.corp_loc_id)+' - '+str(self.date)+' - '+str(self.start_time)+' - '+str(self.end_time)