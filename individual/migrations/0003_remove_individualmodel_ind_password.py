# Generated by Django 2.1.1 on 2018-10-28 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('individual', '0002_auto_20181028_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='individualmodel',
            name='ind_password',
        ),
    ]
