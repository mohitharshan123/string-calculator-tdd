from django.urls import path

from .views import calculate

urlpatterns = [
    path('add/', calculate, name="calculate"),
]
