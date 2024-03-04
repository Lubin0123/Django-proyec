from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'), 
    path('exampletemplate/', views.exampletemplate, name='exampletemplate'),
    path('fruits/', views.fruits, name='fruits'),
    path('cars/', views.cars, name='cars'),
    
    
]