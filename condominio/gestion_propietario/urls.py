from django.urls import path
from . import views

urlpatterns = [
    path('', views.gestion_propietario, name='gestion_propietario'),
    path('carlos', views.gestion_propietario_Copy, name='gestion_propietario_Copy'),
]