# Generated by Django 4.1.1 on 2022-11-12 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='lat',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='lon',
            new_name='longitude',
        ),
    ]