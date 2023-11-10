from rest_framework import serializers

from django.contrib.auth.models import User
from .models import (   
    CustomUser,
    Customer,
    Service,
    ServiceRequest,
    TechnicalAnalysis,
    FinanceEstimate,
    ServiceSchedule,
    ServiceExecution,
    Log,
    ConfigurationSetting,
    GeographicalData,
    LegalCompliance,  
)



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['userType', 'username', 'userId', 'password', 'email']


# Serializers for Customer and related Models
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = '__all__'

class TechnicalAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalAnalysis
        fields = '__all__'

class FinanceEstimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceEstimate
        fields = '__all__'

class ServiceScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceSchedule
        fields = '__all__'

class ServiceExecutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceExecution
        fields = '__all__'

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'

class ConfigurationSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigurationSetting
        fields = '__all__'

class GeographicalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeographicalData
        fields = '__all__'

class LegalComplianceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalCompliance
        fields = '__all__'


