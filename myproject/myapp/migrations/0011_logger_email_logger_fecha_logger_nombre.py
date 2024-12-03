# Generated by Django 5.1.1 on 2024-10-13 02:13

from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_college_logger_alter_student_semester_principal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='logger',
            name='email',
            field=models.EmailField(default='1@1.com', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logger',
            name='fecha',
            field=models.TimeField(default=timezone.now, help_text='Ponga una fecha válida'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logger',
            name='nombre',
            field=models.CharField(default='nulito', max_length=200),
            preserve_default=False,
        ),
    ]
