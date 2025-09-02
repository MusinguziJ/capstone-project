from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from .models import Facility

class FacilityForm(ModelForm):
    class Meta:
        model = Facility
        fields = ['name', 'location', 'facility_type', 'description']

def facility_list(request):
    items = Facility.objects.all().order_by('-created_at')
    return render(request, 'facilities/list.html', {'items': items})

def facility_detail(request, pk):
    item = get_object_or_404(Facility, pk=pk)
    return render(request, 'facilities/detail.html', {'item': item})

def facility_create(request):
    form = FacilityForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('facility_list')
    return render(request, 'facilities/form.html', {'form': form, 'action': 'Add'})

def facility_edit(request, pk):
    item = get_object_or_404(Facility, pk=pk)
    form = FacilityForm(request.POST or None, instance=item)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('facility_detail', pk=item.pk)
    return render(request, 'facilities/form.html', {'form': form, 'action': 'Edit'})

def facility_delete(request, pk):
    item = get_object_or_404(Facility, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('facility_list')
    return render(request, 'facilities/confirm_delete.html', {'item': item})
