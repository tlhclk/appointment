# -*- coding: utf-8 -*-
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from main.models import StreetModel
from django.utils.timezone import now


class IndividualModel(models.Model):
    status=[('1','Married'),('2','Single')]
    gender=[('1','Male'),('2','Female')]
    ind_name=models.CharField(max_length=50)
    ind_lastname=models.CharField(max_length=50)
    ind_email=models.EmailField()
    ind_phone=PhoneNumberField(default='+905554443322')
    ind_rating=models.CharField(max_length=5,default=0.0)
    ind_detail=models.CharField(max_length=200,null=True,blank=True)
    ind_loc_id=models.ForeignKey(StreetModel,on_delete=models.CASCADE,null=True,blank=True)
    ind_no=models.CharField(max_length=11)
    ind_bday=models.DateField()
    ind_statu=models.CharField(max_length=100,choices=status)
    ind_gender=models.CharField(max_length=100,choices=gender,null=True)

    class Meta:
        db_table='individual_table'

    def __str__(self):
        return str(self.ind_name)+' '+str(self.ind_lastname)

    def sta(self):
        return str(dict(self.status)[self.ind_statu])

    def gen(self):
        return str(dict(self.gender)[self.ind_gender])