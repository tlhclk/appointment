# Generated by Django 2.1.1 on 2018-10-28 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_auto_20181027_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointmentmodel',
            name='appointment_id',
        ),
        migrations.AddField(
            model_name='appointmentmodel',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
