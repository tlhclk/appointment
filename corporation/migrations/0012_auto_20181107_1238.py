# Generated by Django 2.0.8 on 2018-11-07 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corporation', '0011_auto_20181107_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corporationmodel',
            name='corp_rep',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='individual.IndividualModel'),
        ),
    ]
