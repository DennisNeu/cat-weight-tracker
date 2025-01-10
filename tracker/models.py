"""Django models, declares data"""

from django.db import models
from django.core.validators import MinValueValidator
from .validators import validate_not_in_future
# Create your models here.


class Cat(models.Model):
    """Class representing a cat"""
    name = models.CharField(max_length=30)
    date_of_birth = models.DateField(
        validators=[validate_not_in_future],
        help_text="Enter the measurement's date"
        )

    initial_weight = models.FloatField(
        validators=[MinValueValidator(0.0)],
        help_text="Enter a positive number"
    )

    def __str__(self):
        return f"{self.name}"


class WeightEntry(models.Model):
    """Class representing a weight entry"""

    class Meta:
        """Meta class"""
        verbose_name_plural = "weight entries"
    cat = models.ForeignKey(
        Cat,
        on_delete=models.CASCADE,
        # Allows accessing a cat's weight entries as `cat.weight_entries`
        related_name="weight_entries"
    )

    date = models.DateField(auto_now_add=True)
    weight = models.FloatField(
        validators=[MinValueValidator(0.0)],
        help_text="Enter a positive number (in kg)"
    )

    def __str__(self):
        return f"Weight: {self.weight} kg on {self.date} for {self.cat.name}"
