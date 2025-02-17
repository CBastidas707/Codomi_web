from django.db import models

# Create your models here.

from django.urls import reverse # Used in get_absolute_url() to get URL for specified ID

from django.db.models import UniqueConstraint # Constrains fields to unique values
from django.db.models.functions import Upper # Returns lower cased value of field

class propietario(models.Model):
    """model que representa a un propietario."""
    d
    nombre = models.CharField(
        max_length=80,
        unique=True,
    )

    def __str__(self):
        """string que representa a un propietario"""
        return self.nombre

    class Meta:
        db_table = 'propietario'
    
class asignacion(models.Model):
    