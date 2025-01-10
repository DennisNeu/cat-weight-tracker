"""defines URL patterns for tracker app"""

from django.urls import path

from . import views

app_name = "tracker"
urlpatterns = [
    # Homepage
    path("", views.index, name="index")
]
