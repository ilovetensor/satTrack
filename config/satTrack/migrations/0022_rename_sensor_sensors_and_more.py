# Generated by Django 4.1.4 on 2023-07-29 17:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('satTrack', '0021_remove_satellite_orbit_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sensor',
            new_name='Sensors',
        ),
        migrations.AlterField(
            model_name='satellite',
            name='last_tle_update',
            field=models.DateField(default=datetime.datetime(2023, 7, 29, 22, 35, 25, 857968), editable=False, verbose_name='Launch Date'),
        ),
        migrations.AlterField(
            model_name='satellite',
            name='launch_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 29, 22, 35, 25, 857968), verbose_name='Launch Date'),
        ),
    ]
