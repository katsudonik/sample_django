from django.shortcuts import render
from django.utils import timezone
from .models import SoilDisposalTask

# Create your views here.
def soil_disposal_tasks_list(request):
    soil_disposal_tasks = SoilDisposalTask.objects.all()
    return render(request, 'polyline/soil_disposal_tasks_list.html', {'soil_disposal_tasks': soil_disposal_tasks})

