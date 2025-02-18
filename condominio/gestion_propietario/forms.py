from django import forms
from .models import Propietario, Correo

class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = ['nombre_prop']

class CorreoForm(forms.ModelForm):
    class Meta:
        model = Correo
        fields = ['correo']
