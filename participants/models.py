from django.db import models

class Participant(models.Model):
    # Choices for Affiliation
    class AffiliationChoices(models.TextChoices):
        COMPUTER_SCIENCE = 'CS', 'Computer Science'
        SOFTWARE_ENGINEERING = 'SE', 'Software Engineering'
        ENGINEERING = 'ENG', 'Engineering'
        OTHER = 'OTHER', 'Other'

    # Choices for Specialization
    class SpecializationChoices(models.TextChoices):
        SOFTWARE = 'SOFTWARE', 'Software'
        HARDWARE = 'HARDWARE', 'Hardware'
        BUSINESS = 'BUSINESS', 'Business'

    # Choices for Institution
    class InstitutionChoices(models.TextChoices):
        SCIT = 'SCIT', 'SCIT'
        CEDAT = 'CEDAT', 'CEDAT'
        UNIPOD = 'UNIPOD', 'UniPod'
        UIRI = 'UIRI', 'UIRI'
        LWERA = 'LWERA', 'Lwera'

    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True) # Ensures no duplicate emails
    affiliation = models.CharField(max_length=10, choices=AffiliationChoices.choices)
    specialization = models.CharField(max_length=20, choices=SpecializationChoices.choices)
    cross_skill_trained = models.BooleanField(default=False)
    institution = models.CharField(max_length=20, choices=InstitutionChoices.choices)

    def __str__(self):
        return f"{self.full_name} ({self.affiliation})"