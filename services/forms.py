# services/forms.py
from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['facility', 'name', 'description', 'category', 'skill_type']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap form-control class to all form fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'