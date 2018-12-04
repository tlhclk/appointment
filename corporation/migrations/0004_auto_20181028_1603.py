# Generated by Django 2.1.1 on 2018-10-28 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corporation', '0003_corpservicemodel_ratingmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointmenthourmodel',
            name='app_hour_id',
        ),
        migrations.RemoveField(
            model_name='corplocmodel',
            name='corp_loc_id',
        ),
        migrations.RemoveField(
            model_name='corporationmodel',
            name='corp_id',
        ),
        migrations.RemoveField(
            model_name='corpservicemodel',
            name='corp_service_id',
        ),
        migrations.RemoveField(
            model_name='ratingmodel',
            name='rating_id',
        ),
        migrations.AddField(
            model_name='appointmenthourmodel',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='corplocmodel',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='corporationmodel',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='corpservicemodel',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ratingmodel',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
