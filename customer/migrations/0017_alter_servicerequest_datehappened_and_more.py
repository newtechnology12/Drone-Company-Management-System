# Generated by Django 4.2 on 2023-09-01 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0016_alter_servicerequest_businesstype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='DateHappened',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='District',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
