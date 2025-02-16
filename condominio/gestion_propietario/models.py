from django.db import models

# Create your models here.

from django.urls import reverse # Used in get_absolute_url() to get URL for specified ID

from django.db.models import UniqueConstraint # Constrains fields to unique values
from django.db.models.functions import Lower # Returns lower cased value of field

class propietario(models.Model):
    """model que representara a un propietario."""
    nombre = models.CharField(
        max_length=80,
        unique=True,
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    class Meta:
        db_table = 'propietario'
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='genre_name_case_insensitive_unique',
                violation_error_message = "Genre already exists (case insensitive match)"
            ),
        ]
    