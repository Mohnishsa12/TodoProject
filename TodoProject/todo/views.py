from django.shortcuts import render
from .models import Task
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.



def verifytask(request,userid):
    Task.objects.filter(id=userid).update(status=True)
    return redirect("home")

def addtask(request):
    data = request.POST['task1']
    Task.objects.create(task=data)
    return redirect("home")