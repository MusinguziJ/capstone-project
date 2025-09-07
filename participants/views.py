from django.shortcuts import render, get_object_or_404, redirect
from .models import Participant
from .forms import ParticipantForm
from django.http import HttpResponse  # ← ADD THIS IMPORT

def participant_list(request):
    participants = Participant.objects.all()
    return render(request, 'participants/participant_list.html', {'participants': participants})

def participant_detail(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    return render(request, 'participants/participant_detail.html', {'participant': participant})

def participant_create(request):
    print("=== DEBUG: participant_create view called ===")
    print(f"Request method: {request.method}")
    
    if request.method == 'POST':
        print("DEBUG: POST request received")
        form = ParticipantForm(request.POST)
        print(f"DEBUG: Form is valid: {form.is_valid()}")
        
        if form.is_valid():
            print("DEBUG: Form is valid - saving participant")
            participant = form.save()
            print(f"DEBUG: Participant saved: {participant}")
            return redirect('participants:list')
        else:
            print(f"DEBUG: Form errors: {form.errors}")
    else:
        print("DEBUG: GET request - showing empty form")
        form = ParticipantForm()
    
    print("DEBUG: About to render template...")
    
    # Test if template rendering works
    try:
        response = render(request, 'participants/participant_form.html', {'form': form, 'title': 'Add New Participant'})
        print(f"DEBUG: Template rendered successfully, content length: {len(response.content)}")
        return response
    except Exception as e:
        print(f"DEBUG: Template rendering failed: {e}")
        return HttpResponse(f"Template error: {e}")

def participant_update(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            return redirect('participants:detail', pk=participant.pk)
    else:
        form = ParticipantForm(instance=participant)
    return render(request, 'participants/participant_form.html', {'form': form, 'title': f'Edit {participant.full_name}'})

def participant_delete(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    if request.method == 'POST':
        participant.delete()
        return redirect('participants:list')
    return render(request, 'participants/participant_confirm_delete.html', {'participant': participant})