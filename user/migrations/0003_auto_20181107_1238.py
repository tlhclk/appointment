# Generated by Django 2.0.8 on 2018-11-07 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corporation', '0012_auto_20181107_1238'),
        ('user', '0002_auto_20181027_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='corporation_id',
        ),
        migrations.AddField(
            model_name='user',
            name='corp_loc_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='corporation.CorpLocModel'),
        ),
    ]
