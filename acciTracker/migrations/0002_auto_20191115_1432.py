# Generated by Django 2.2.7 on 2019-11-15 14:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acciTracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accident',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 15, 14, 32, 11, 427900)),
        ),
        migrations.AlterField(
            model_name='crowd',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 15, 14, 32, 11, 428222)),
        ),
    ]
