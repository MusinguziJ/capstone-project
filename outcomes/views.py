from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import FileResponse, Http404
from django.contrib.auth.decorators import login_required
from .models import Outcome
from .forms import OutcomeForm
from projects.models import Project

@login_required
def project_selection(request):
    """Page to select a project to view outcomes"""
    projects = Project.objects.all()
    return render(request, 'outcomes/project_selection.html', {'projects': projects})

@login_required
def outcome_list(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    outcomes = Outcome.objects.filter(project=project)
    return render(request, 'outcomes/outcome_list.html', {
        'outcomes': outcomes,
        'project': project
    })

@login_required
def outcome_detail(request, pk):
    outcome = get_object_or_404(Outcome, pk=pk)
    return render(request, 'outcomes/outcome_detail.html', {'outcome': outcome})

@login_required
def outcome_create(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    
    if request.method == 'POST':
        form = OutcomeForm(request.POST, request.FILES)
        if form.is_valid():
            outcome = form.save(commit=False)
            outcome.project = project
            outcome.save()
            messages.success(request, 'Outcome created successfully!')
            return redirect('outcomes:list', project_id=project.id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = OutcomeForm()
    
    return render(request, 'outcomes/outcome_form.html', {
        'form': form,
        'project': project,
        'title': 'Add New Outcome'
    })

@login_required
def outcome_update(request, pk):
    outcome = get_object_or_404(Outcome, pk=pk)
    
    if request.method == 'POST':
        form = OutcomeForm(request.POST, request.FILES, instance=outcome)
        if form.is_valid():
            form.save()
            messages.success(request, 'Outcome updated successfully!')
            return redirect('outcomes:detail', pk=outcome.pk)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = OutcomeForm(instance=outcome)
    
    return render(request, 'outcomes/outcome_form.html', {
        'form': form,
        'outcome': outcome,
        'title': f'Edit Outcome: {outcome.title}'
    })

@login_required
def outcome_delete(request, pk):
    outcome = get_object_or_404(Outcome, pk=pk)
    project_id = outcome.project.id
    
    if request.method == 'POST':
        outcome.delete()
        messages.success(request, 'Outcome deleted successfully!')
        return redirect('outcomes:list', project_id=project_id)
    
    return render(request, 'outcomes/outcome_confirm_delete.html', {'outcome': outcome})

@login_required
def download_artifact(request, pk):
    outcome = get_object_or_404(Outcome, pk=pk)
    if outcome.artifact_file:
        return FileResponse(outcome.artifact_file.open(), as_attachment=True)
    raise Http404("No file available for download")