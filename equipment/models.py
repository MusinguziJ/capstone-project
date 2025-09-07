from django.db import models
from facilities.models import Facility

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)  # Link to Facility
    capabilities = models.TextField(blank=True)  # What it can do
    usage_domain = models.CharField(max_length=50, blank=True)  # Electronics, Mechanical, IoT
    support_phase = models.CharField(max_length=50, blank=True)  # Training, Prototyping, Testing

    def __str__(self):
        return self.name


class EquipmentFile(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name="files")
    file = models.FileField(upload_to='equipment_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} for {self.equipment.name}"
