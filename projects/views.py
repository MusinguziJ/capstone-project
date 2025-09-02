from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, ProjectParticipant
from .forms import ProjectForm, ProjectParticipantForm
from participants.models import Participant

def project_list(request):
    projects = Project.objects.all().select_related('program', 'facility')
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    participants = project.participants.all()
    assigned_participants = ProjectParticipant.objects.filter(project=project).select_related('participant')
    
    # Handle form submission for adding participants
    if request.method == 'POST' and 'add_participant' in request.POST:
        form = ProjectParticipantForm(request.POST)
        if form.is_valid():
            project_participant = form.save(commit=False)
            project_participant.project = project
            project_participant.save()
            return redirect('projects:detail', pk=project.pk)
    else:
        form = ProjectParticipantForm()
    
    context = {
        'project': project,
        'participants': participants,
        'assigned_participants': assigned_participants,
        'form': form,
        'available_participants': Participant.objects.exclude(id__in=participants.values_list('id', flat=True))
    }
    return render(request, 'projects/project_detail.html', context)

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects:list')
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form, 'title': 'Create New Project'})

def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects:detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/project_form.html', {'form': form, 'title': f'Edit {project.title}'})

def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects:list')
    return render(request, 'projects/project_confirm_delete.html', {'project': project})

# ADD THIS NEW VIEW FOR REMOVING PARTICIPANTS
def remove_participant(request, project_pk, participant_pk):
    project = get_object_or_404(Project, pk=project_pk)
    participant = get_object_or_404(Participant, pk=participant_pk)
    
    if request.method == 'POST':
        # Remove the participant from the project
        ProjectParticipant.objects.filter(project=project, participant=participant).delete()
        return redirect('projects:detail', pk=project.pk)
    
    return render(request, 'projects/confirm_remove_participant.html', {
        'project': project,
        'participant': participant
    })