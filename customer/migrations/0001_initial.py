# Generated by Django 4.2 on 2023-08-21 11:53

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('Cell_List', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('Cell_List_Description', models.CharField(max_length=80)),
                ('Sector_List_Description', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'Cell',
            },
        ),
        migrations.CreateModel(
            name='ConfigurationSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setting_name', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('customerId', models.CharField(blank=True, max_length=16, null=True, unique=True)),
                ('contact_information', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(blank=True, max_length=80, null=True)),
                ('Status', models.CharField(blank=True, max_length=80, null=True)),
                ('gender', models.CharField(blank=True, max_length=80, null=True)),
                ('education', models.CharField(blank=True, max_length=80, null=True)),
                ('province', models.CharField(blank=True, max_length=80, null=True)),
                ('district', models.CharField(blank=True, max_length=80, null=True)),
                ('sector', models.CharField(blank=True, max_length=80, null=True)),
                ('cell', models.CharField(blank=True, max_length=80, null=True)),
                ('village', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('District_List', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('District_List_Description', models.CharField(max_length=80)),
                ('Province_List_Description', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'District',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('Education_Description', models.CharField(blank=True, max_length=255, primary_key=True, serialize=False)),
                ('interface', models.CharField(blank=True, max_length=15)),
            ],
            options={
                'db_table': 'Education',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('gender', models.CharField(blank=True, max_length=15, primary_key=True, serialize=False)),
                ('GenderDescription', models.CharField(blank=True, max_length=15)),
                ('interface', models.CharField(blank=True, max_length=15)),
            ],
            options={
                'db_table': 'Customer_Gender',
            },
        ),
        migrations.CreateModel(
            name='GeographicalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=255)),
                ('coordinates', models.CharField(max_length=255)),
                ('elevation', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='LegalCompliance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requirement_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Marital_Status',
            fields=[
                ('Marital_Status', models.CharField(blank=True, max_length=5, primary_key=True, serialize=False)),
                ('Marital_Status_Description', models.CharField(blank=True, max_length=20)),
                ('interface', models.CharField(blank=True, max_length=15)),
            ],
            options={
                'db_table': 'Marital_Status',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('Province_List', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('Province_List_Description', models.CharField(max_length=80, null=True)),
            ],
            options={
                'db_table': 'Province',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=255)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.service')),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('Village_List', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('Vilage_List_Description', models.CharField(max_length=80)),
                ('Cell_List_Description', models.CharField(max_length=40)),
                ('Cell_List', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.cell')),
            ],
            options={
                'db_table': 'Village',
            },
        ),
        migrations.CreateModel(
            name='TechnicalAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analysis_date', models.DateTimeField(auto_now_add=True)),
                ('technical_details', models.TextField()),
                ('feasibility', models.BooleanField()),
                ('service_request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer.servicerequest')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheduled_date_time', models.DateTimeField()),
                ('drone_team_assigned', models.CharField(max_length=255)),
                ('service_request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer.servicerequest')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceExecution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('execution_date_time', models.DateTimeField()),
                ('technical_details', models.TextField()),
                ('status', models.CharField(max_length=255)),
                ('service_schedule', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer.serviceschedule')),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('Sector_List', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('Sector_List_Description', models.CharField(max_length=80)),
                ('District_List_Description', models.CharField(max_length=80)),
                ('District_List', models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.PROTECT, to='customer.district')),
            ],
            options={
                'db_table': 'Sector',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FinanceEstimate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estimate_date', models.DateTimeField(auto_now_add=True)),
                ('cost_details', models.DecimalField(decimal_places=2, max_digits=10)),
                ('service_request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer.servicerequest')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='Province_List',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.PROTECT, to='customer.province'),
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[('admin', 'Admin'), ('welcome_team', 'Welcome Team'), ('technical_team', 'Technical Team'), ('finance', 'Finance'), ('drone_operator', 'Drone Operator')], max_length=20)),
                ('groups', models.ManyToManyField(related_name='customuser_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='customuser_set', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='cell',
            name='Sector_List',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.sector'),
        ),
    ]