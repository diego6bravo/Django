# Generated by Django 5.1.1 on 2024-10-13 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_remove_logger_fecha'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logger',
            options={'permissions': [('can_edit_email', 'Can edit email')]},
        ),
    ]
