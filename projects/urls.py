from django.urls import path
from . import views

urlpatterns = [
    path('', views.project),
    path('projects/', views.projects),
]
