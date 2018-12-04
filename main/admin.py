# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import ProvinceModel,TownModel,DistrictModel,StreetModel,ServiceModel
from django.contrib import admin


admin.site.register(ProvinceModel)
admin.site.register(TownModel)
admin.site.register(DistrictModel)
admin.site.register(StreetModel)
admin.site.register(ServiceModel)