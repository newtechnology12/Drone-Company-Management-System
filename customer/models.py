from django.contrib.auth.models import AbstractUser,Group,Permission
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

class Province(models.Model):
    Province_List = models.CharField(primary_key=True, unique=True, max_length=10, blank=False, null=False)
    Province_List_Description = models.CharField(max_length=80, blank=False, null=True)

    def __str__(self) -> str:
        return self.Province_List_Description

    class Meta:
        db_table = 'Province'


class District(models.Model):
    District_List = models.CharField(primary_key=True, unique=True, max_length=10, blank=False, null=False)
    District_List_Description = models.CharField(max_length=80, blank=False, null=False)
    Province_List = models.ForeignKey(Province, on_delete=models.PROTECT, max_length=10, blank=False, null=False)
    Province_List_Description = models.CharField(max_length=80, blank=False, null=False)

    def __str__(self) -> str:
        return self.District_List_Description

    class Meta:
        db_table = 'District'


class Sector(models.Model):
    Sector_List = models.CharField(primary_key=True, unique=True, max_length=10, blank=False, null=False)
    Sector_List_Description = models.CharField(max_length=80, blank=False, null=False)
    District_List = models.ForeignKey(District, max_length=10, on_delete=models.PROTECT, blank=False, null=False)
    District_List_Description = models.CharField(max_length=80, blank=False, null=False)

    def __str__(self) -> str:
        return self.Sector_List_Description

    class Meta:
        db_table = 'Sector'


class Cell(models.Model):
    Cell_List = models.CharField(primary_key=True, unique=True, max_length=10, blank=False, null=False)
    Cell_List_Description = models.CharField(max_length=80, blank=False, null=False)
    Sector_List = models.ForeignKey(Sector, on_delete=models.PROTECT, blank=False, null=False)
    Sector_List_Description = models.CharField(max_length=80, blank=False, null=False)

    def __str__(self) -> str:
        return self.Cell_List_Description

    class Meta:
        db_table = 'Cell'


class Village(models.Model):
    Village_List = models.CharField(primary_key=True, unique=True, max_length=20, blank=False, null=False)
    Vilage_List_Description = models.CharField(max_length=80, blank=False, null=False)
    Cell_List = models.ForeignKey(Cell, on_delete=models.PROTECT, blank=False, null=False)
    Cell_List_Description = models.CharField(max_length=40, blank=False, null=False)

    def __str__(self) -> str:
        return self.Vilage_List_Description

    class Meta:
        db_table = 'Village'


class Marital_Status(models.Model):
    Marital_Status = models.CharField(primary_key=True, max_length=5, blank=True, null=False)
    Marital_Status_Description = models.CharField(max_length=20, blank=True, null=False)
    interface = models.CharField(max_length=15, blank=True, null=False)

    def __str__(self):
        return self.Marital_Status_Description

    class Meta:
        db_table = 'Marital_Status'


class Education(models.Model):
    Education_Description = models.CharField(primary_key=True, max_length=255, blank=True, null=False)
    interface = models.CharField(max_length=15, blank=True, null=False)

    def __str__(self):
        return self.Education_Description

    class Meta:
        db_table = 'Education'


class Gender(models.Model):
    gender = models.CharField(primary_key=True, max_length=15, blank=True, null=False)
    GenderDescription = models.CharField(max_length=15, blank=True, null=False)
    interface = models.CharField(max_length=15, blank=True, null=False)

    def __str__(self):
        return self.gender

    class Meta:
        db_table = 'Customer_Gender'


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (

        ('workerTeam', 'workerTeam'),
        ('techninicalTeam', 'techninicalTeam'),
        ('drone_operator', 'drone_operator'),
    )
    userType = models.CharField(max_length=80, choices=USER_TYPE_CHOICES, blank=True, null=True)
    username = models.CharField(unique=True, max_length=80, blank=True, null=True)
    userId = models.CharField(max_length=80, blank=True, null=True)
    password = models.CharField(max_length=80, blank=True, null=True)
    email = models.EmailField(max_length=80, blank=True, null=True)

    def __str__(self):
        return self.username



class Customer(models.Model):
    name = models.CharField(max_length=255)
    customerId = models.CharField(max_length=16, unique=True, blank=True, null=True)
    contact_information = models.CharField(max_length=255, blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=80, blank=True, null=True)
    Status = models.CharField(max_length=80, blank=True, null=True)
    phone = models.CharField(max_length=80, blank=True, null=True)
    gender = models.CharField(max_length=80, blank=True, null=True)
    education = models.CharField(max_length=80, blank=True, null=True)
    province = models.CharField(max_length=80, blank=True, null=True)
    district = models.CharField(max_length=80, blank=True, null=True)
    sector = models.CharField(max_length=80, blank=True, null=True)
    cell = models.CharField(max_length=80, blank=True, null=True)
    village = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    service_name = models.CharField(max_length=255, blank=True, null=True)
    UserId =models.CharField(max_length=255, blank=True, null=True)
    fullName = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    TinNumber=models.CharField(max_length=80, blank=True, null=True)
    Dete =models.CharField(max_length=80, blank=True, null=True)
    DescriptionoftheActivity=models.CharField(max_length=500, blank=True, null=True)
    LocationofTheActivity = models.CharField(max_length=500, blank=True, null=True)
    Activity_province = models.CharField(max_length=80, blank=True, null=True)
    Activity_district = models.CharField(max_length=80, blank=True, null=True)
    Activity_sector = models.CharField(max_length=80, blank=True, null=True)
    Activity_cell = models.CharField(max_length=80, blank=True, null=True)
    Activity_village = models.CharField(max_length=80, blank=True, null=True)
    aerialPhotographyCheckbox = models.BooleanField(default=False, blank=True, null=True)
    roundwithprecisionagriculture= models.BooleanField(default=False, blank=True, null=True)
    photographyandvideography= models.BooleanField(default=False, blank=True, null=True)
    Preciselaborsavingoperations= models.BooleanField(default=False, blank=True, null=True)
    Mining= models.BooleanField(default=False, blank=True, null=True)
    Mapping= models.BooleanField(default=False, blank=True, null=True)
    orthophotoCheckbox= models.BooleanField(default=False, blank=True, null=True)
    aerialSurveyCheckbox= models.BooleanField(default=False, blank=True, null=True)
    aerialSprayingCheckbox= models.BooleanField(default=False, blank=True, null=True)
    ndviCheckbox= models.BooleanField(default=False, blank=True, null=True)
    otherInformationCheckbox= models.BooleanField(default=False, blank=True, null=True)
    Signature=  models.CharField(max_length=80, blank=True, null=True)
     

class ServiceRequest(models.Model):
    customerNationalId = models.CharField(max_length=255, blank=True, null=True)
    serviceName = models.CharField(max_length=255, blank=True, null=True)
    serviceLocation = models.CharField(max_length=255, blank=True, null=True)
    TinNumber=models.CharField(max_length=80, blank=True, null=True)
    District = models.CharField(max_length=255, blank=True, null=True)
    DateHappened = models.CharField(max_length=255, blank=True, null=True)
    BusinessType = models.CharField(max_length=80, blank=True, null=True)
    
    TaskActivityDetails = models.TextField(max_length=2000)
    ApprovedBy = models.CharField(max_length=255, blank=True, null=True)
    comment =models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"{self.customerNationalId} - {self.serviceName}"


class TechnicalAnalysis(models.Model):
    nationalId = models.CharField(max_length=255, blank=True, null=True)
    technical_details = models.TextField()
    
    location=models.CharField(max_length=255, blank=True, null=True)
    searchTIN=models.CharField(max_length=255, blank=True, null=True)
    approvedBy=models.CharField(max_length=255, blank=True, null=True)
    comment=models.CharField(max_length=255, blank=True, null=True)
    district=models.CharField(max_length=255, blank=True, null=True)
    dateHappened=models.CharField(max_length=255, blank=True, null=True)
    businessCategory=models.CharField(max_length=255, blank=True, null=True)
   
    def __str__(self):
        return f"Analysis for {self.technical_details}"


class FinanceEstimate(models.Model):
    service_request = models.OneToOneField(ServiceRequest, on_delete=models.CASCADE)
    estimate_date = models.DateTimeField(auto_now_add=True)
    cost_details = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Estimate for {self.service_request}"


class ServiceSchedule(models.Model):
    service_request = models.OneToOneField(ServiceRequest, on_delete=models.CASCADE)
    scheduled_date_time = models.DateTimeField()
    drone_team_assigned = models.CharField(max_length=255)

    def __str__(self):
        return f"Schedule for {self.service_request}"


class ServiceExecution(models.Model):
    service_schedule = models.OneToOneField(ServiceSchedule, on_delete=models.CASCADE)
    execution_date_time = models.DateTimeField()
    technical_details = models.TextField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"Execution for {self.service_schedule}"


class Log(models.Model):
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"{self.action} at {self.timestamp}"


class ConfigurationSetting(models.Model):
    setting_name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.setting_name


class GeographicalData(models.Model):
    location_name = models.CharField(max_length=255)
    coordinates = models.CharField(max_length=255)
    elevation = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.location_name


class LegalCompliance(models.Model):
    SearchName = models.CharField(max_length=255,null=True,blank=True)
    contact_info = models.TextField(null=True,blank=True)
    technical_details = models.CharField(max_length=255,null=True,blank=True)
    location = models.CharField(max_length=255,null=True,blank=True)
    approvedBy = models.CharField(max_length=255,null=True,blank=True)
    Message = models.CharField(max_length=255,null=True,blank=True)
    uploadReport = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.SearchName

