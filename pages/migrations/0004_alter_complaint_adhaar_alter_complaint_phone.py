# Generated by Django 4.1.1 on 2022-11-12 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_complaint_delete_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='adhaar',
            field=models.IntegerField(max_length=12),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='phone',
            field=models.IntegerField(max_length=10),
        ),
    ]
