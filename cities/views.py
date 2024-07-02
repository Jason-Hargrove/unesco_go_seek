from django.shortcuts import render
from django.http import JsonResponse
from .models import City
import random

def index(request):
    return render(request, 'index.html')

def random_city(request):
    city = random.choice(City.objects.all())
    return JsonResponse({
        'name': city.name,
        'country': city.country,
        'specialization': city.specialization
    })