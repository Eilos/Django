# Generated by Django 4.0.3 on 2022-06-13 08:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0016_remove_personnel_machine_machine_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 8, 6, 38, 540627)),
        ),
    ]
