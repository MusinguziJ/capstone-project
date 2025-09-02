from django.db import models

class Program(models.Model):
    # Choices for FocusAreas
    class FocusAreaChoices(models.TextChoices):
        IOT = 'IOT', 'IoT'
        AUTOMATION = 'AUTOMATION', 'Automation'
        RENEWABLE_ENERGY = 'RENEWABLE_ENERGY', 'Renewable Energy'
        AI_ML = 'AI_ML', 'AI/ML'
        ROBOTICS = 'ROBOTICS', 'Robotics'

    # Choices for Phases
    class PhaseChoices(models.TextChoices):
        CROSS_SKILLING = 'CROSS_SKILLING', 'Cross-Skilling'
        COLLABORATION = 'COLLABORATION', 'Collaboration'
        TECHNICAL_SKILLS = 'TECHNICAL_SKILLS', 'Technical Skills'
        PROTOTYPING = 'PROTOTYPING', 'Prototyping'
        COMMERCIALIZATION = 'COMMERCIALIZATION', 'Commercialization'

    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    national_alignment = models.CharField(max_length=300, help_text="Link to NDPIII, Roadmap, or 4IR goals")
    focus_areas = models.CharField(max_length=100, choices=FocusAreaChoices.choices)
    phases = models.CharField(max_length=100, choices=PhaseChoices.choices)

    def __str__(self):
        return self.name