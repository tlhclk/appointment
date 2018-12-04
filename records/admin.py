# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import AppointmentModel,RatingModel
from django.contrib import admin


admin.site.register(AppointmentModel)
admin.site.register(RatingModel)