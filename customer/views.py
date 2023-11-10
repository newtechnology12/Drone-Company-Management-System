
from rest_framework import generics, permissions
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.shortcuts import render
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
    LegalCompliance, Province,District,Sector,Cell,Village,Gender,Marital_Status,Education
)
from .serializers import (
    CustomUserSerializer,
    CustomerSerializer,
    ServiceSerializer,
    ServiceRequestSerializer,
    TechnicalAnalysisSerializer,
    FinanceEstimateSerializer,
    ServiceScheduleSerializer,
    ServiceExecutionSerializer,
    LogSerializer,
    ConfigurationSettingSerializer,
    GeographicalDataSerializer,
    LegalComplianceSerializer,
)

class CustomUserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


# Mixin class to add authentication and authorization to views
class AuthenticationAndAuthorizationMixin:
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated, UserTypePermission]


# Customer views
class CustomerListCreateView(AuthenticationAndAuthorizationMixin,generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDestroyView(AuthenticationAndAuthorizationMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# Service views
class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

# ServiceRequest views
class ServiceRequestListCreateView(generics.ListCreateAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer

class ServiceRequestRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer

# TechnicalAnalysis views
class TechnicalAnalysisListCreateView(generics.ListCreateAPIView):
    queryset = TechnicalAnalysis.objects.all()
    serializer_class = TechnicalAnalysisSerializer

class TechnicalAnalysisRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TechnicalAnalysis.objects.all()
    serializer_class = TechnicalAnalysisSerializer

# FinanceEstimate views
class FinanceEstimateListCreateView(generics.ListCreateAPIView):
    queryset = FinanceEstimate.objects.all()
    serializer_class = FinanceEstimateSerializer

class FinanceEstimateRetrieveUpdateDestroyView(AuthenticationAndAuthorizationMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = FinanceEstimate.objects.all()
    serializer_class = FinanceEstimateSerializer

# ServiceSchedule views
class ServiceScheduleListCreateView(generics.ListCreateAPIView):
    queryset = ServiceSchedule.objects.all()
    serializer_class = ServiceScheduleSerializer

class ServiceScheduleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceSchedule.objects.all()
    serializer_class = ServiceScheduleSerializer

# ServiceExecution views
class ServiceExecutionListCreateView(generics.ListCreateAPIView):
    queryset = ServiceExecution.objects.all()
    serializer_class = ServiceExecutionSerializer

class ServiceExecutionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceExecution.objects.all()
    serializer_class = ServiceExecutionSerializer

# Log views
class LogListCreateView(generics.ListCreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

class LogRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

# ConfigurationSetting views
class ConfigurationSettingListCreateView(generics.ListCreateAPIView):
    queryset = ConfigurationSetting.objects.all()
    serializer_class = ConfigurationSettingSerializer

class ConfigurationSettingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConfigurationSetting.objects.all()
    serializer_class = ConfigurationSettingSerializer

# GeographicalData views
class GeographicalDataListCreateView(generics.ListCreateAPIView):
    queryset = GeographicalData.objects.all()
    serializer_class = GeographicalDataSerializer

class GeographicalDataRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GeographicalData.objects.all()
    serializer_class = GeographicalDataSerializer

# LegalCompliance views
class LegalComplianceListCreateView(generics.ListCreateAPIView):
    queryset = LegalCompliance.objects.all()
    serializer_class = LegalComplianceSerializer

class LegalComplianceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LegalCompliance.objects.all()
    serializer_class = LegalComplianceSerializer



def Genderdata (request):
    gender  = list(Gender.objects.values())
    return JsonResponse(gender, safe=False)

def Educationdata (request):
    education  = list(Education.objects.values())
    return JsonResponse(education, safe=False)

def Marital_Statusdata (request):
    owndamage  = list(Marital_Status.objects.values())
    return JsonResponse(owndamage, safe=False)

def Provincedata (request):
    theft =  list(Province.objects.values())
    return JsonResponse(theft, safe=False)


def Districtdata(request):
    fire = list(District.objects.values())
    return JsonResponse(fire, safe=False)


def Sectordata(request):
    excess = list(Sector.objects.values())
    return JsonResponse(excess, safe=False)

def Celldata(request):
    occupant = list(Cell.objects.values())
    return JsonResponse(occupant, safe=False)

def Villagedata(request):
    fees = list(Village.objects.values())
    return JsonResponse(fees, safe=False)
