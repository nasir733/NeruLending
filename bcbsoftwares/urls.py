from django.urls import path
from . import views
urlpatterns = [
    path('bcbvideosoftware/', views.bcbvideosoftware, name='index'),
    path('bcbprojectmanagment/', views.bcbprojectmanagment,
         name='bcbprojectmanagment'),
    path('bcbcrmsoftware/', views.bcbcrmsoftware, name='bcbcrmsoftware'),
    path('bcbappointmentsoftware/',
         views.bcbappointmentsoftware, name="appointment"),
]
