# Generated by Django 4.2 on 2023-09-01 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0018_remove_customuser_userid_alter_customuser_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='userId',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]