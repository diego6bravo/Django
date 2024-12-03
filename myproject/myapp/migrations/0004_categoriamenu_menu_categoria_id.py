# Generated by Django 5.1.1 on 2024-10-07 22:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_referenciassku_referencias'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrecategoria', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='categoria_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='myapp.categoriamenu'),
        ),
    ]