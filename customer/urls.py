from django.urls import path
from . import views

urlpatterns = [
    # CustomUser views
    path('customusers/', views.CustomUserListCreateView.as_view(), name='customuser-list'),
    path('customusers/<int:pk>/', views.CustomUserRetrieveUpdateDestroyView.as_view(), name='customuser-detail'),

    # Customer views
    path('customers/', views.CustomerListCreateView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', views.CustomerRetrieveUpdateDestroyView.as_view(), name='customer-detail'),

    # Service views
    path('services/', views.ServiceListCreateView.as_view(), name='service-list'),
    path('services/<int:pk>/', views.ServiceRetrieveUpdateDestroyView.as_view(), name='service-detail'),

    # ServiceRequest views
    path('servicerequests/', views.ServiceRequestListCreateView.as_view(), name='servicerequest-list'),
    path('servicerequests/<int:pk>/', views.ServiceRequestRetrieveUpdateDestroyView.as_view(), name='servicerequest-detail'),

    # TechnicalAnalysis views
    path('technicalanalyses/', views.TechnicalAnalysisListCreateView.as_view(), name='technicalanalysis-list'),
    path('technicalanalyses/<int:pk>/', views.TechnicalAnalysisRetrieveUpdateDestroyView.as_view(), name='technicalanalysis-detail'),

    # FinanceEstimate views
    path('financeestimates/', views.FinanceEstimateListCreateView.as_view(), name='financeestimate-list'),
    path('financeestimates/<int:pk>/', views.FinanceEstimateRetrieveUpdateDestroyView.as_view(), name='financeestimate-detail'),

    # ServiceSchedule views
    path('serviceschedules/', views.ServiceScheduleListCreateView.as_view(), name='serviceschedule-list'),
    path('serviceschedules/<int:pk>/', views.ServiceScheduleRetrieveUpdateDestroyView.as_view(), name='serviceschedule-detail'),

    # ServiceExecution views
    path('serviceexecutions/', views.ServiceExecutionListCreateView.as_view(), name='serviceexecution-list'),
    path('serviceexecutions/<int:pk>/', views.ServiceExecutionRetrieveUpdateDestroyView.as_view(), name='serviceexecution-detail'),

    # Log views
    path('logs/', views.LogListCreateView.as_view(), name='log-list'),
    path('logs/<int:pk>/', views.LogRetrieveUpdateDestroyView.as_view(), name='log-detail'),

    # ConfigurationSetting views
    path('configurationsettings/', views.ConfigurationSettingListCreateView.as_view(), name='configurationsetting-list'),
    path('configurationsettings/<int:pk>/', views.ConfigurationSettingRetrieveUpdateDestroyView.as_view(), name='configurationsetting-detail'),

    # GeographicalData views
    path('geographicaldata/', views.GeographicalDataListCreateView.as_view(), name='geographicaldata-list'),
    path('geographicaldata/<int:pk>/', views.GeographicalDataRetrieveUpdateDestroyView.as_view(), name='geographicaldata-detail'),

    # LegalCompliance views
    path('legalcompliance/', views.LegalComplianceListCreateView.as_view(), name='legalcompliance-list'),
    path('legalcompliance/<int:pk>/', views.LegalComplianceRetrieveUpdateDestroyView.as_view(), name='legalcompliance-detail'),
    path('Educationdata/', views.Educationdata, name='Educationdata'),
    path('Genderdata/', views.Genderdata, name='Patient_Genderdata'),
    path('Marital_Statusdata/', views.Marital_Statusdata, name='Marital_Statusdata'),
    path('Provincedata/', views.Provincedata, name='Provincedata'),
    path('Districtdata/', views.Districtdata, name='Districtdata'),
    path('Sectordata/', views.Sectordata, name='Sectordata'),
    path('Celldata/', views.Celldata, name='Celldata'),
    path('Villagedata/', views.Villagedata, name='Villagedata'),
]
