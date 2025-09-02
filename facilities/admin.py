from django.contrib import admin
from .models import Facility

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'facility_type', 'location', 'created_at')
    search_fields = ('name', 'location', 'facility_type')
