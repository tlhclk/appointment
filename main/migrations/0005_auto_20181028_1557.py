# Generated by Django 2.1.1 on 2018-10-28 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_servicemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicemodel',
            name='service_id',
        ),
        migrations.AddField(
            model_name='servicemodel',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
