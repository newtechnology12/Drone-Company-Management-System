# Generated by Django 4.2 on 2023-08-25 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_rename_cell_service_activity_cell_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='UserId',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='fullName',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
