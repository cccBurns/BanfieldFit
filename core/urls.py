from django.urls import path
from . import views
from core.views import inicio, planes, contacto, horarios, about

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about/', views.about, name='about'),
    path('planes/', views.planes, name='planes'),
    path('horarios/', views.horarios, name='horarios'),
    path('contacto/', views.contacto, name='contacto'),
]