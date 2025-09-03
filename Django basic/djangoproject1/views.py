from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employess
def home(request):
    emp = Employess.objects.all()
    context={
        'employees':emp
    }
    # print(employees)  
    return render(request,'hello.html',context)

def dynamicdata(request):
    emp = Employess.objects.all()
    context = {
        'employees':emp
    }
    return render(request,"DynamicData.html",context)