from django.urls import pathfrom 
from . import views

urlpatterns = [
    path('',views.index),
]