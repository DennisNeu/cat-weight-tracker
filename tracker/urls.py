"""defines URL patterns for tracker app"""

from django.urls import path
from . import views

app_name = "tracker"
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    path('cat/<int:cat_id>/weights/', views.cat_weights, name='cat_weights'),
    path('cat/<int:cat_id>/weights/new/', views.new_weight_entry, name='new_weight_entry'),
]
