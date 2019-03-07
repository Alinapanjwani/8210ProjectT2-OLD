from django.contrib import admin

from .models import Bed
from events.models import Organization, Event

# Register your models here.
class BedList(admin.ModelAdmin):
    list_display=('event_id', 'org_id', 'org_name', 'bed_type', 'initial_num_available')
    list_filter=('event_id', 'bed_type')
    ordering=['org_name']

admin.site.register(Bed)