from django.urls import path
from . import views
urlpatterns = [
    path('<int:userid>/', views.employe_details,name="employe_detail")
]