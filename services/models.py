# services/models.py
from django.db import models

# --- PLACEHOLDER MODEL FOR TESTING - REMOVE LATER ---
# This is a temporary model so we can work without the real 'facilities' app.
# TODO: REMOVE THIS AFTER THE REAL 'FACILITIES' APP IS CREATED BY ANOTHER TEAMMATE
class Facility(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)  # 'blank=True' makes it optional in forms

    def __str__(self):
        return self.name
# --- END PLACEHOLDER MODEL ---

# Your actual Service model starts here
class Service(models.Model):
    # Categories a service can belong to
    class CategoryChoices(models.TextChoices):
        MACHINING = 'MACHINING', 'Machining'
        TESTING = 'TESTING', 'Testing'
        TRAINING = 'TRAINING', 'Training'

    # Types of skills required for the service
    class SkillTypeChoices(models.TextChoices):
        HARDWARE = 'HARDWARE', 'Hardware'
        SOFTWARE = 'SOFTWARE', 'Software'
        INTEGRATION = 'INTEGRATION', 'Integration'

    # Link to the Facility model. If the facility is deleted, delete all its services too (CASCADE)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CategoryChoices.choices)
    skill_type = models.CharField(max_length=50, choices=SkillTypeChoices.choices)

    def __str__(self):
        return f"{self.name} ({self.facility.name})"