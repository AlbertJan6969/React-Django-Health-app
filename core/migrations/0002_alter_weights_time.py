# Generated by Django 4.2.1 on 2023-05-17 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weights',
            name='time',
            field=models.DateField(default='2023-05-17'),
        ),
    ]
