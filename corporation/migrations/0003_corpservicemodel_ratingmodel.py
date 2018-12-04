# Generated by Django 2.1.1 on 2018-10-23 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('individual', '0001_initial'),
        ('main', '0004_servicemodel'),
        ('corporation', '0002_auto_20181021_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorpServiceModel',
            fields=[
                ('corp_service_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('details', models.CharField(max_length=200)),
                ('corp_loc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corporation.CorpLocModel')),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ServiceModel')),
            ],
            options={
                'db_table': 'corp_service_table',
            },
        ),
        migrations.CreateModel(
            name='RatingModel',
            fields=[
                ('rating_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=5)),
                ('details', models.CharField(max_length=200)),
                ('corp_loc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corporation.CorpLocModel')),
                ('ind_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='individual.IndividualModel')),
            ],
            options={
                'db_table': 'rating_table',
            },
        ),
    ]
