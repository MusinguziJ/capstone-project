from django.shortcuts import render, get_object_or_404, redirect
from .models import Participant
from .forms import ParticipantForm

def participant_list(request):
    participants = Participant.objects.all()
    return render(request, 'participants/participant_list.html', {'participants': participants})

def participant_detail(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    return render(request, 'participants/participant_detail.html', {'participant': participant})

def participant_create(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participants:list')
    else:
        form = ParticipantForm()
    return render(request, 'participants/participant_form.html', {'form': form, 'title': 'Add New Participant'})

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