from django.db import models
from programs.models import Program  # Import the Program model you just built
from facilities.models import Facility  # Import the Facility model from your teammate
from participants.models import Participant

class Project(models.Model):
    # Choices for NatureOfProject
    class NatureOfProjectChoices(models.TextChoices):
        RESEARCH = 'RESEARCH', 'Research'
        PROTOTYPE = 'PROTOTYPE', 'Prototype'
        APPLIED_WORK = 'APPLIED_WORK', 'Applied Work'

    # Choices for InnovationFocus
    class InnovationFocusChoices(models.TextChoices):
        IOT_DEVICES = 'IOT_DEVICES', 'IoT devices'
        SMART_HOME = 'SMART_HOME', 'Smart home'
        RENEWABLE_ENERGY = 'RENEWABLE_ENERGY', 'Renewable energy'
        AI_SOLUTIONS = 'AI_SOLUTIONS', 'AI solutions'
        ROBOTICS = 'ROBOTICS', 'Robotics'

    # Choices for PrototypeStage
    class PrototypeStageChoices(models.TextChoices):
        CONCEPT = 'CONCEPT', 'Concept'
        PROTOTYPE = 'PROTOTYPE', 'Prototype'
        MVP = 'MVP', 'Minimum Viable Product (MVP)'
        MARKET_LAUNCH = 'MARKET_LAUNCH', 'Market Launch'

    # ForeignKeys to Program and Facility (your dependencies)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='projects')
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='projects')
    
    # Core fields from the PDF specification
    title = models.CharField(max_length=300)
    nature_of_project = models.CharField(max_length=50, choices=NatureOfProjectChoices.choices)
    description = models.TextField()
    innovation_focus = models.CharField(max_length=50, choices=InnovationFocusChoices.choices)
    prototype_stage = models.CharField(max_length=50, choices=PrototypeStageChoices.choices)
    testing_requirements = models.TextField(blank=True)
    commercialization_plan = models.TextField(blank=True)

    # ADD THIS: Many-to-many relationship through ProjectParticipant
    participants = models.ManyToManyField(
        Participant, 
        through='ProjectParticipant', 
        related_name='projects',
        blank=True
    )

    def __str__(self):
        return f"{self.title} ({self.program.name})"

# ADD THIS COMPLETE MODEL DEFINITION
class ProjectParticipant(models.Model):
    # Choices for RoleOnProject
    class RoleChoices(models.TextChoices):
        STUDENT = 'STUDENT', 'Student'
        LECTURER = 'LECTURER', 'Lecturer'
        CONTRIBUTOR = 'CONTRIBUTOR', 'Contributor'
        MENTOR = 'MENTOR', 'Mentor'

    # Choices for SkillRole
    class SkillRoleChoices(models.TextChoices):
        DEVELOPER = 'DEVELOPER', 'Developer'
        ENGINEER = 'ENGINEER', 'Engineer'
        DESIGNER = 'DESIGNER', 'Designer'
        BUSINESS_LEAD = 'BUSINESS_LEAD', 'Business Lead'
        RESEARCHER = 'RESEARCHER', 'Researcher'
        TESTER = 'TESTER', 'Tester'

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    role_on_project = models.CharField(max_length=20, choices=RoleChoices.choices, default=RoleChoices.STUDENT)
    skill_role = models.CharField(max_length=20, choices=SkillRoleChoices.choices, default=SkillRoleChoices.DEVELOPER)

    class Meta:
        # Ensure a participant can only be assigned once to a project
        unique_together = [['project', 'participant']]

    def __str__(self):
        return f"{self.participant.full_name} - {self.project.title} ({self.role_on_project})"