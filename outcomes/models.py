from django.db import models
from projects.models import Project  # Make sure you have Project model

class Outcome(models.Model):
    OUTCOME_TYPES = [
        ('CAD', 'CAD Design'),
        ('PCB', 'PCB Design'),
        ('PROTOTYPE', 'Prototype'),
        ('REPORT', 'Report'),
        ('BUSINESS_PLAN', 'Business Plan'),
        ('SOFTWARE', 'Software'),
        ('DOCUMENTATION', 'Documentation'),
    ]
    
    COMMERCIALIZATION_STATUS = [
        ('DEFINED', 'Defined'),
        ('MARKET_LINKED', 'Market Linked'),
        ('LAUNCHED', 'Launched'),
    ]
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='outcomes')
    title = models.CharField(max_length=200)
    description = models.TextField()
    artifact_link = models.URLField(blank=True, null=True)
    artifact_file = models.FileField(upload_to='outcomes/', blank=True, null=True)
    outcome_type = models.CharField(max_length=20, choices=OUTCOME_TYPES)
    quality_certification = models.TextField(blank=True, null=True)
    commercialization_status = models.CharField(max_length=20, choices=COMMERCIALIZATION_STATUS, default='DEFINED')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.get_outcome_type_display()}"

    class Meta:
        ordering = ['-created_at']