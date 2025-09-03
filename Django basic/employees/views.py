from django.shortcuts import render
from .models import Employess
from django.http import Http404, HttpResponse
# Create your views here.


# HttpResponse Example
# def employe_details(request,userid):
#     try:
#         emp = Employess.objects.get(id=userid)
#         print(emp)
#         return HttpResponse(emp)
#     except:
#         raise Http404


# Http Template Example

def employe_details(request,userid):
    try:
        emp = Employess.objects.get(id=userid)
        context = {
            'employe':emp
        }

        return render(request,"employe_details.html",context)
    except:
        raise Http404
        
    
