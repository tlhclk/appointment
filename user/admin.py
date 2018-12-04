# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User,AbstractUser
from django.contrib import admin


admin.register(User)
admin.register(AbstractUser)
