from django.contrib import admin

from .models import Organization, Event, Nurse

# Register your models here.
class OrgList(admin.ModelAdmin):
    list_display=('org_id', 'org_name', 'org_type')
    list_filter=('org_name', 'org_type')
    ordering=['org_name']

class EventList(admin.ModelAdmin):
    list_display=('event_id', 'event_type', 'event_start_date', 'event_end_date')
    list_filter=('event_id', 'event_type', 'event_start_date')
    ordering=['event_id']

class NurseList(admin.ModelAdmin):
    list_display=('user', 'org_name', 'phone')
    list_filter=('org_name')
    ordering=['org_name']

admin.site.register(Organization)
admin.site.register(Event)
admin.site.register(Nurse)

