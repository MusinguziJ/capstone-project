from django import forms
from .models import Equipment, EquipmentFile

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'capabilities', 'usage_domain', 'support_phase', 'facility', 'available', 'description']

class EquipmentFileForm(forms.ModelForm):
    class Meta:
        model = EquipmentFile
        fields = ['file']
