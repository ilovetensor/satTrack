# Generated by Django 4.1.4 on 2023-07-31 17:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('satTrack', '0048_alter_satellite_last_tle_update_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='satellite',
            name='last_tle_update',
            field=models.DateField(default=datetime.datetime(2023, 7, 31, 22, 32, 44, 548204), editable=False, verbose_name='Launch Date'),
        ),
        migrations.AlterField(
            model_name='satellite',
            name='launch_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 31, 22, 32, 44, 548204), verbose_name='Launch Date'),
        ),
    ]