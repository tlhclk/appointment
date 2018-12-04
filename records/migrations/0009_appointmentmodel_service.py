# Generated by Django 2.0.8 on 2018-11-09 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corporation', '0013_reservedhourmodel'),
        ('records', '0008_auto_20181108_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentmodel',
            name='service',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='corporation.CorpServiceModel'),
            preserve_default=False,
        ),
    ]
