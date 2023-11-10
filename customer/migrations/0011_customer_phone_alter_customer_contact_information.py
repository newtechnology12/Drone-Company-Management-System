# Generated by Django 4.2 on 2023-08-26 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_remove_service_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='contact_information',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
