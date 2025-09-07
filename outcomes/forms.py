from django import forms
from .models import Outcome

class OutcomeForm(forms.ModelForm):
    class Meta:
        model = Outcome
        fields = [
            'title', 'description', 'outcome_type', 
            'artifact_link', 'artifact_file', 
            'quality_certification', 'commercialization_status'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe the outcome...'}),
            'quality_certification': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Certification details...'}),
            'title': forms.TextInput(attrs={'placeholder': 'Outcome title'}),
            'artifact_link': forms.URLInput(attrs={'placeholder': 'https://...'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        artifact_link = cleaned_data.get('artifact_link')
        artifact_file = cleaned_data.get('artifact_file')
        
        if not artifact_link and not artifact_file:
            raise forms.ValidationError("Either artifact link or artifact file must be provided.")
        
        return cleaned_data