# -*- coding: utf-8 -*-
from django.db import models


class ProvinceModel(models.Model):
    province_id=models.CharField(max_length=2,primary_key=True)
    province_title=models.CharField(max_length=50)

    class Meta:
        db_table='province_table'

    def __str__(self):
        return str(self.province_title)


class TownModel(models.Model):
    town_id=models.CharField(max_length=20,primary_key=True)
    town_title=models.CharField(max_length=50)
    province_id=models.ForeignKey(ProvinceModel,on_delete=models.CASCADE)

    class Meta:
        db_table='town_table'

    def __str__(self):
        return str(self.town_title)+' - '+str(self.province_id)


class DistrictModel(models.Model):
    district_id=models.CharField(max_length=20,primary_key=True)
    district_title=models.CharField(max_length=50)
    town_id=models.ForeignKey(TownModel,on_delete=models.CASCADE)

    class Meta:
        db_table='district_table'

    def __str__(self):
        return str(self.district_title)+' - '+str(self.town_id)


class StreetModel(models.Model):
    street_id=models.CharField(max_length=20,primary_key=True)
    street_title=models.CharField(max_length=50)
    district_id=models.ForeignKey(DistrictModel,on_delete=models.CASCADE)

    class Meta:
        db_table='street_table'

    def __str__(self):
        return str(self.street_title)+' - '+str(self.district_id)



class ServiceModel(models.Model):
    service_title=models.CharField(max_length=50)
    service_detail=models.CharField(max_length=200,null=True,blank=True)

    class Meta:
        db_table='service_table'

    def __str__(self):
        return str(self.service_title)
