# Generated by Django 4.2 on 2023-09-11 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0021_remove_technicalanalysis_analysis_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='legalcompliance',
            name='description',
        ),
        migrations.RemoveField(
            model_name='legalcompliance',
            name='requirement_name',
        ),
        migrations.RemoveField(
            model_name='legalcompliance',
            name='status',
        ),
        migrations.AddField(
            model_name='legalcompliance',
            name='Message',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legalcompliance',
            name='SearchName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legalcompliance',
            name='approvedBy',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legalcompliance',
            name='contact_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legalcompliance',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legalcompliance',
            name='technical_details',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='legalcompliance',
            name='uploadReport',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]