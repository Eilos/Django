# Generated by Django 4.0.3 on 2022-06-13 08:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0018_alter_machine_maintenancedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnel',
            name='machine',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='computerApp.machine'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 8, 7, 29, 20500)),
        ),
    ]
