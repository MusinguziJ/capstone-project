# services/forms.py
from django import forms
from .models import Service  # This imports your Service model

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['facility', 'name', 'description', 'category', 'skill_type']