# Generated by Django 4.1.4 on 2023-07-29 08:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('satTrack', '0007_alter_satellite_launch_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='satellite',
            name='launch_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 29, 13, 50, 12, 981701), verbose_name='Launch Date'),
        ),
    ]
