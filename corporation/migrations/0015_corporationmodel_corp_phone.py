# Generated by Django 2.1.3 on 2018-11-25 12:55

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('corporation', '0014_auto_20181117_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='corporationmodel',
            name='corp_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+905554443322', max_length=128),
        ),
    ]
