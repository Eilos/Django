# Generated by Django 4.0.3 on 2022-06-12 22:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0009_alter_machine_maintenancedate'),
    ]

    operations = [
        migrations.CreateModel(
            name='infrastructure',
            fields=[
                ('lieu', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('machines', models.IntegerField()),
                ('manager', models.CharField(max_length=20)),
                ('employe', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 12, 22, 59, 6, 127325)),
        ),
    ]