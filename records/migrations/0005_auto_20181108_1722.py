# Generated by Django 2.0.8 on 2018-11-08 14:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_appointmentmodel_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointmentmodel',
            name='day',
        ),
        migrations.RemoveField(
            model_name='appointmentmodel',
            name='month',
        ),
        migrations.RemoveField(
            model_name='appointmentmodel',
            name='year',
        ),
        migrations.AddField(
            model_name='appointmentmodel',
            name='date',
            field=models.DateField(default=datetime.date(2018, 11, 8)),
        ),
    ]
