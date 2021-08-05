from django.urls import path
from . import views
urlpatterns=[
    path('bcbvideosoftware/',views.bcbvideosoftware,name='index'),
]