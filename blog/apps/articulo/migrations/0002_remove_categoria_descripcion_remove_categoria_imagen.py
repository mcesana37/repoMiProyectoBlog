# Generated by Django 4.2.3 on 2023-07-12 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='imagen',
        ),
    ]
