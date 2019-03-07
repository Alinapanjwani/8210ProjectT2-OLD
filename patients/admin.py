from django.contrib import admin

from .models import Patient, PatientTrackingHeader, PatientTrackingDetail, PatientTrackingInjuries, PatientTrackingDisposition
from events.models import Organization, Event
from beds.models import Bed

# Register your models here.
class PatientList(admin.ModelAdmin):
    list_display=('patient_last_name', 'patient_first_name', 'patient_middle_name', 'next_of_kin_name', 'next_of_kin_relation', 'next_of_kin_phone')
    list_filter=('patient_id', 'patient_last_name')
    search_fields=('patient_last_name', 'patient_id')
    ordering=['patient_last_name']

class PatientTrackingList(admin.ModelAdmin):
    list_display=('patient_id', 'event_id', 'org_id', 'org_name', 'patient_last_name', 'patient_first_name', )
    list_filter=('patient_id', 'org_id')
    search_fields=('patint_id', 'org_id', 'org_name', 'patient_last_name', 'patient_first_name')
    ordering=['patient_last_name']

class PatientTrackingDetailList(admin.ModelAdmin):
    list_display=('tracking_id', 'patient_id', 'patient_last_name', 'patient_first_name', 'triage_tag_num', 'tag_color_condition', 'mode_of_arrival','room_number', 'arrival_date')
    list_filter=('patient_id', 'tracking_id', 'triage_tag_num', 'patient_last_name')
    search_fields=('patient_id', 'tracking_id', 'triage_tag_num', 'patient_last_name')
    ordering=['patient_last_name', 'tag_color_condition']

class PatientTrackingInjuriesList(admin.ModelAdmin):
    list_display=('patient_id', 'patient_last_name', 'patient_first_name', 'injury_type')
    list_filter=()
    search_fields=()
    ordering=['patient_last_name']

class PatientTrackingDispositionList(admin.ModelAdmin):
    list_display=('patient_id', 'patient_last_name', 'patient_first_name', 'disposition_type', 'transfer_to_org_id', 'updated_cndition', 'time_of_death')
    list_filter=()
    search_fields=()
    ordering=['patient_last_name']


admin.site.register(Patient)
admin.site.register(PatientTrackingHeader)
admin.site.register(PatientTrackingDetail)
admin.site.register(PatientTrackingInjuries)
admin.site.register(PatientTrackingDisposition)