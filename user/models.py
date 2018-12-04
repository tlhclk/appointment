# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
from individual.models import IndividualModel
from corporation.models import CorpLocModel,CorporationModel

class User(AbstractUser):
    individual_id=models.ForeignKey(IndividualModel,on_delete=models.CASCADE,null=True,blank=True)
    corporation_id=models.ForeignKey(CorporationModel,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.email)
