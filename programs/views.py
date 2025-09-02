from django.shortcuts import render, get_object_or_404, redirect
from .models import Program
from .forms import ProgramForm

def program_list(request):
    programs = Program.objects.all()
    return render(request, 'programs/program_list.html', {'programs': programs})

def program_detail(request, pk):
    program = get_object_or_404(Program, pk=pk)
    return render(request, 'programs/program_detail.html', {'program': program})

def program_create(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('programs:list')
    else:
        form = ProgramForm()
    return render(request, 'programs/program_form.html', {'form': form, 'title': 'Create New Program'})

def program_update(request, pk):
    program = get_object_or_404(Program, pk=pk)
    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            return redirect('programs:detail', pk=program.pk)
    else:
        form = ProgramForm(instance=program)
    return render(request, 'programs/program_form.html', {'form': form, 'title': f'Edit {program.name}'})

def program_delete(request, pk):
    program = get_object_or_404(Program, pk=pk)
    if request.method == 'POST':
        program.delete()
        return redirect('programs:list')
    return render(request, 'programs/program_confirm_delete.html', {'program': program})