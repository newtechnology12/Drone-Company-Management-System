from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *


class ProvinceResources(resources.ModelResource):
    class Meta:
        model = Province
        import_id_fields = ('Province_List',)
        fields =('Province_List','Province_List_Description',)

@admin.register(Province)
class ProvinceAdmin(ImportExportModelAdmin):
    resource_class = ProvinceResources
    list_display = ('Province_List','Province_List_Description')

class DistrictAdmin(resources.ModelResource):
    class Meta:
        model = District
        import_id_fields = ('District_List',)
        fields = ('District_List','District_List_Description','Province_List','Province_List_Description',)

@admin.register(District)
class DistrictAdmin(ImportExportModelAdmin):
    resource_class = DistrictAdmin
    list_display = ('District_List','District_List_Description','Province_List','Province_List_Description')

class Sectorresources(resources.ModelResource):
    class Meta:
        model = Sector
        import_id_fields = ('Sector_List',)
        fields = ('Sector_List','Sector_List_Description','District_List','District_List_Description',)
@admin.register(Sector)
class SectorAdmin(ImportExportModelAdmin):
    resource_class = Sectorresources
    list_display = ('Sector_List','Sector_List_Description','District_List','District_List_Description')


class CellResources(resources.ModelResource):
    class Meta:
        model = Cell
        import_id_fields = ('Cell_List',)
        fields = ('Cell_List','Cell_List_Description','Sector_List','Sector_List_Description',)
        
@admin.register(Cell)
class CellAdmin(ImportExportModelAdmin):
    resource_class = CellResources
    list_display = ('Cell_List','Cell_List_Description','Sector_List','Sector_List_Description')
class VillageResources(resources.ModelResource):
    class Meta:
        model = Village
        import_id_fields = ('Village_List',)
        fields = ('Village_List','Vilage_List_Description','Cell_List','Cell_List_Description',)

@admin.register(Village)
class VillageAdmin(ImportExportModelAdmin):
    resource_class = VillageResources
    list_display = ('Village_List','Vilage_List_Description','Cell_List','Cell_List_Description')

class EducationResource(resources.ModelResource):
    class Meta:
        model = Education
        import_id_fields = ('Education_Description',)
        fields = ('Education_Description','interface',) 

@admin.register(Education)
class EducationAdmin(ImportExportModelAdmin):
    resource_class = EducationResource
    list_display = ('Education_Description','interface')



class Marital_StatusResources(resources.ModelResource):
    class Meta:
        model = Marital_Status
        import_id_fields = ('Marital_Status',)
        fields = ('Marital_Status','Marital_Status_Description','interface',)
@admin.register(Marital_Status)
class Marital_StatusAdmin(ImportExportModelAdmin):
    resource_class = Marital_StatusResources
    list_display = ('Marital_Status','Marital_Status_Description','interface')


class GenderResource(resources.ModelResource):

    class Meta:
        model = Gender
        import_id_fields = ('gender',)
        fields = ('gender','GenderDescription','interface',) 

@admin.register(Gender)
class GenderAdmin(ImportExportModelAdmin):
    resource_class = GenderResource
    list_display = ('gender','GenderDescription','interface')




admin.site.register(CustomUser)
admin.site.register(Customer)
admin.site.register(User)
admin.site.register(Service)
admin.site.register(ServiceRequest)

admin.site.register(TechnicalAnalysis)
admin.site.register(FinanceEstimate)
admin.site.register(ServiceSchedule)

admin.site.register(ServiceExecution)
admin.site.register(Log)
admin.site.register(ConfigurationSetting)

admin.site.register(GeographicalData)
admin.site.register(LegalCompliance)
