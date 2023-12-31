# Generated by Django 4.1.4 on 2023-07-29 16:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('satTrack', '0012_sensors_satellite_orbit_satellite_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='satellite',
            name='swath',
            field=models.FloatField(default=0, verbose_name='Swath [km]'),
        ),
        migrations.AlterField(
            model_name='satellite',
            name='last_tle_update',
            field=models.DateField(default=datetime.datetime(2023, 7, 29, 22, 3, 42, 872108), editable=False, verbose_name='Launch Date'),
        ),
        migrations.AlterField(
            model_name='satellite',
            name='launch_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 29, 22, 3, 42, 872108), verbose_name='Launch Date'),
        ),
    ]
