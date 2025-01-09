from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class Cat(models.Model):
    """Class representing a cat"""

    name = models.CharField(max_length=30)
    date_of_birth = models.CharField(max_length=30) # Figure out how to use actual dates
    initial_weight = models.FloatField(
        validators=[MinValueValidator(0.0)],
        help_text="Enter a positive number"
    )
    def __str__(self):
        return f"{self.name}"