from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('planes/', views.planes, name='planes'),
    path('horarios/', views.horarios, name='horarios'),
    path('contacto/', views.contacto, name='contacto'),
]