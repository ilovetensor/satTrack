# Generated by Django 4.1.4 on 2023-07-29 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('satTrack', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Satellites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Posts',
        ),
    ]