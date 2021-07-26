from django.urls import path
from . import views

urlpatterns = [
    path('project/', views.project),
    path('project/<str:pk>/', views.pro),
]
