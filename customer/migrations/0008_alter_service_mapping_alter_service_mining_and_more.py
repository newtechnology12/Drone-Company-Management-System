# Generated by Django 4.2 on 2023-08-25 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_service_mapping_service_mining_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='Mapping',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='Mining',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='Preciselaborsavingoperations',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='Signature',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='UserId',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='aerialPhotographyCheckbox',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='aerialSprayingCheckbox',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='aerialSurveyCheckbox',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='fullName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='ndviCheckbox',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='orthophotoCheckbox',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='otherInformationCheckbox',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='photographyandvideography',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='roundwithprecisionagriculture',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
