from django.db import models

# Create your models here.

from django.urls import reverse # Used in get_absolute_url() to get URL for specified ID

from django.db.models import UniqueConstraint # Constrains fields to unique values
from django.db.models.functions import Upper # Returns lower cased value of field

class Propietario(models.Model):
    """model que representa a un propietario."""
    id_prop = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)

    def __str__(self):
        """string que representa a un propietario"""
        return self.nombre

    class Meta:
        db_table = 'propietario'
    
class Dpto(models.Model):
    nro_dpto = models.IntegerField(primary_key=True)
    alicuota = models.DecimalField(max_digits=4, decimal_places=2)
    id_edif = models.IntegerField()

    def __str__(self):
        return self.nro_dpto
    
    class Meta:
        db_table = 'dpto'

class Asignacion(models.Model):
    id_prop = models.ForeignKey(Propietario, on_delete=models.CASCADE, db_column='id_propietario')
    nro_dpto = models.ForeignKey(Dpto, on_delete=models.CASCADE, db_column='nro_dpto')
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField(null=True, blanl=True)

    def __str__(self):
        return  f"Asignación de {self.id_propietario} a {self.nro_dpto} desde {self.fecha_inicio} hasta {self.fecha_fin or 'presente'}"
    
    class Meta:
        db_table = 'asignacion'
        unique_together = (('id_propietario', 'nro_dpto', 'fecha_inicio'))