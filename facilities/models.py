from django.db import models

class Facility(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200, blank=True)
    facility_type = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Facilities"