# Generated by Django 5.1.1 on 2024-11-28 20:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volgtekapp', '0006_visit_time_alter_visit_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hall',
            name='opening_hours',
        ),
        migrations.AddField(
            model_name='hall',
            name='end_time',
            field=models.TimeField(default='21:00'),
        ),
        migrations.AddField(
            model_name='hall',
            name='start_time',
            field=models.TimeField(default='09:00'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 11, 28, 23, 7, 8, 968478)),
        ),
        migrations.AlterField(
            model_name='visit',
            name='time',
            field=models.TimeField(default=datetime.time(23, 7, 8, 968483)),
        ),
    ]