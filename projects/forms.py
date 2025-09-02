from django import forms
from .models import Project, ProjectParticipant

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['program', 'facility', 'title', 'nature_of_project', 'description', 
                 'innovation_focus', 'prototype_stage', 'testing_requirements', 
                 'commercialization_plan']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap styling
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.Select, forms.Textarea)):
                field.widget.attrs['class'] = 'form-control'
            # Make textareas larger
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs['rows'] = 3

# ADD THIS NEW FORM
class ProjectParticipantForm(forms.ModelForm):
    class Meta:
        model = ProjectParticipant
        fields = ['participant', 'role_on_project', 'skill_role']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap styling
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'