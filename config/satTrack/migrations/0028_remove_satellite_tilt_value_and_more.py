# Generated by Django 4.1.4 on 2023-07-29 17:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('satTrack', '0027_alter_satellite_last_tle_update_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='satellite',
            name='tilt_value',
        ),
        migrations.AlterField(
            model_name='satellite',
            name='last_tle_update',
            field=models.DateField(default=datetime.datetime(2023, 7, 29, 22, 43, 41, 168857), editable=False, verbose_name='Launch Date'),
        ),
        migrations.AlterField(
            model_name='satellite',
            name='launch_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 29, 22, 43, 41, 168857), verbose_name='Launch Date'),
        ),
    ]