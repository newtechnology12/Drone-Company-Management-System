# Generated by Django 4.2 on 2023-09-01 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0017_alter_servicerequest_datehappened_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='userId',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='userType',
            field=models.CharField(blank=True, choices=[('workerTeam', 'workerTeam'), ('techninicalTeam', 'techninicalTeam'), ('drone_operator', 'drone_operator')], max_length=80, null=True),
        ),
    ]