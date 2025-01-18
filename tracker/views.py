from django.shortcuts import render
from .models import Cat
from django.http import Http404
# Create your views here.


def index(request):
    """Homepage"""
    cats = Cat.objects.all().prefetch_related('weight_entries')
    cats_with_weight = [
        {
            'cat': cat,
            'last_weight': cat.weight_entries.order_by('date').last()
        }
        for cat in cats
    ]

    return render(
        request,
        'tracker/index.html',
        {"cats_with_weight": cats_with_weight}
        )


def cat_weights(request, cat_id):
    try:
        cat = Cat.objects.get(id=cat_id)
        weight_entries = cat.weight_entries.order_by('date')
    except Cat.DoesNotExist:
        raise Http404("Cat does not exist")

    return render(
        request,
        'tracker/weights.html',
        {
            'cat': cat,
            'weight_entries': weight_entries,
        }

    )


def new_weight_entry(request, cat_id):
    cats = Cat.objects.all()

    return render(
        request,
        'tracker/new_weight.html',
        {
         'cats': cats
        }
    )
