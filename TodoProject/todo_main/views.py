from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task
def home(request):
    task = Task.objects.filter(status=False).order_by("-createdAt")
    completedTask = Task.objects.filter(status=True).order_by("-createdAt")
    context = {
        "tasklist":task,
        "completetask":completedTask
    }
    return render(request,"home.html",context)