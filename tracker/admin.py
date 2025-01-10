from django.contrib import admin

from .models import Cat, WeightEntry

# Register your models here.

admin.site.register(Cat)
admin.site.register(WeightEntry)
