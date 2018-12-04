# Generated by Django 2.1.1 on 2018-10-21 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0003_auto_20181021_1720'),
        ('corporation', '0001_initial'),
        ('individual', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='corporationmodel',
            name='corp_rep',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='individual.IndividualModel'),
        ),
        migrations.AddField(
            model_name='corplocmodel',
            name='corporation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corporation.CorporationModel'),
        ),
        migrations.AddField(
            model_name='corplocmodel',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.StreetModel'),
        ),
        migrations.AddField(
            model_name='appointmenthourmodel',
            name='corp_loc_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corporation.CorpLocModel'),
        ),
    ]
