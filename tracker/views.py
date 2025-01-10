from django.shortcuts import render
from .models import Cat
# Create your views here.


def index(request):
    """Homepage"""
    cats = Cat.objects.all().prefetch_related('weight_entries')
    cats_with_weight = [
        {
            'cat': cat,
            'last_weight': cat.weight_entries.order_by('-date').first()
        }
        for cat in cats
    ]

    return render(
        request,
        'tracker/index.html',
        {"cats_with_weight": cats_with_weight}
        )


def cat_weights(request):
    return


def new_weightdjango_entry():
    return
