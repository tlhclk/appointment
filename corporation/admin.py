# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import CorporationModel,CorpLocModel,AppointmentHourModel,CorpServiceModel,ReservedHourModel
from django.contrib import admin


admin.site.register(CorporationModel)
admin.site.register(CorpLocModel)
admin.site.register(AppointmentHourModel)
admin.site.register(CorpServiceModel)
admin.site.register(ReservedHourModel)
