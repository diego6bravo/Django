# Generated by Django 5.1.1 on 2024-10-14 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuRest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=200)),
                ('precio', models.CharField(max_length=200)),
            ],
        ),
    ]