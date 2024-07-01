from django.urls import path
from .views import index, random_city

urlpatterns = [
    path('', index, name='index'),
    path('random/', random_city, name='random_city'),
]