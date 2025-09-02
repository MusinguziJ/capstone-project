# services/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Service
from .forms import ServiceForm

def service_list(request):
    """Read: List all services"""
    services = Service.objects.all().select_related('facility') # Optimize DB queries
    return render(request, 'services/service_list.html', {'services': services})

def service_detail(request, pk):
    """Read: Get a single service's details"""
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'services/service_detail.html', {'service': service})

def service_create(request):
    """Create: Handle form submission for a new service"""
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            new_service = form.save()
            return redirect('services:detail', pk=new_service.pk)
    else:
        form = ServiceForm()
    return render(request, 'services/service_form.html', {'form': form, 'title': 'Create New Service'})

def service_update(request, pk):
    """Update: Handle form submission to edit an existing service"""
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('services:detail', pk=service.pk)
    else:
        form = ServiceForm(instance=service)
    return render(request, 'services/service_form.html', {'form': form, 'title': f'Edit {service.name}'})

def service_delete(request, pk):
    """Delete: Handle deleting a service"""
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('services:list')
    return render(request, 'services/service_confirm_delete.html', {'service': service})