# Generated by Django 5.1.1 on 2024-11-29 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volgtekapp', '0012_remove_hall_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='time',
            field=models.CharField(max_length=5),
        ),
    ]
