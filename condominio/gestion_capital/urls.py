from django.urls import path
from .views import ImporteListView  

urlpatterns = [
    path('importes/', ImporteListView.as_view(), name='importe_list'),
]