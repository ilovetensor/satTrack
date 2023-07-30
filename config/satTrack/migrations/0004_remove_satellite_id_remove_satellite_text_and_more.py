# Generated by Django 4.1.4 on 2023-07-29 05:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('satTrack', '0003_rename_satellites_satellite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='satellite',
            name='id',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='text',
        ),
        migrations.AddField(
            model_name='satellite',
            name='description',
            field=models.TextField(default='description not provided', verbose_name='About Satellite'),
        ),
        migrations.AddField(
            model_name='satellite',
            name='launch_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 29, 11, 13, 22, 754349), verbose_name='Launch Date'),
        ),
        migrations.AddField(
            model_name='satellite',
            name='launch_site',
            field=models.CharField(default='not provided', max_length=50, verbose_name='Launch Site'),
        ),
        migrations.AddField(
            model_name='satellite',
            name='name',
            field=models.CharField(default='name', max_length=20, verbose_name='Satellite Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='satellite',
            name='norad_id',
            field=models.IntegerField(default=123, primary_key=True, serialize=False, verbose_name='NORAD ID'),
            preserve_default=False,
        ),
    ]
