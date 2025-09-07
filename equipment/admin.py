from django.contrib import admin
from .models import Equipment, EquipmentFile

class EquipmentFileInline(admin.TabularInline):
    model = EquipmentFile
    extra = 1

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'available')
    search_fields = ('name',)
    inlines = [EquipmentFileInline]
