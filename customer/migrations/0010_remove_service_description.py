# Generated by Django 4.2 on 2023-08-25 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_alter_service_signature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='description',
        ),
    ]
