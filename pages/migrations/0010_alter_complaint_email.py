# Generated by Django 4.1.1 on 2022-11-12 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_complaint_address_witness_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='email',
            field=models.EmailField(blank=True, max_length=50),
        ),
    ]
