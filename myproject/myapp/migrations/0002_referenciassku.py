# Generated by Django 5.1.1 on 2024-10-07 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferenciasSKU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plu', models.CharField(max_length=100)),
                ('codsap', models.CharField(max_length=100)),
                ('marca_vehiculo', models.CharField(max_length=100)),
            ],
        ),
    ]
