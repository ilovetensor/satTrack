# Generated by Django 4.1.4 on 2023-07-30 13:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('satTrack', '0046_alter_satellite_last_tle_update_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='satellite',
            name='last_tle_update',
            field=models.DateField(default=datetime.datetime(2023, 7, 30, 19, 2, 42, 383560), editable=False, verbose_name='Launch Date'),
        ),
        migrations.AlterField(
            model_name='satellite',
            name='launch_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 30, 19, 2, 42, 383560), verbose_name='Launch Date'),
        ),
    ]
