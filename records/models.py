# -*- coding: utf-8 -*-
from django.db import models
from individual.models import IndividualModel
from corporation.models import AppointmentHourModel,ReservedHourModel,CorpServiceModel,CorpLocModel,CorporationModel
from django.utils import timezone




class AppointmentModel(models.Model):
    person_id=models.ForeignKey(IndividualModel,on_delete=models.CASCADE)
    res_hour_id=models.ForeignKey(ReservedHourModel,on_delete=models.CASCADE)
    service=models.ForeignKey(CorpServiceModel,on_delete=models.CASCADE)
    detail=models.CharField(max_length=200,null=True,blank=True)


    class Meta:
        db_table='appointment'

    def __str__(self):
        return str(self.res_hour_id)+' - '+str(self.person_id)

    #def appointment_detail(self):
        #return str(self.corp_loc_id)+str(self.person_id)+str(self.date)+str(self.hour)



class RatingModel(models.Model):
    corp_id=models.ForeignKey(CorporationModel,on_delete=models.CASCADE,null=True,blank=True)
    ind_id=models.ForeignKey(IndividualModel,on_delete=models.CASCADE,null=True,blank=True)
    value=models.CharField(max_length=5)
    details=models.CharField(max_length=200,null=True,blank=True)

    class Meta:
        db_table='rating_table'

    def __str__(self):
        return str(self.corp_id)+' - '+str(self.ind_id)+' - '+str(self.value)+' - '+str(self.details)
