# Generated by Django 5.1.1 on 2024-10-13 02:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_remove_logger_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='logger',
            name='fecha',
            field=models.TimeField(default=django.utils.timezone.now, help_text='Ponga una fecha válida'),
        ),
    ]
