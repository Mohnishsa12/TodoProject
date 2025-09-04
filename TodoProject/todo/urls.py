from . import views
from django.urls import path

urlpatterns = [
    path("verifytask/<int:userid>/",views.verifytask,name="verifytask"),
    path("addtask/",views.addtask,name="addtask"),
]