from django.shortcuts import render
from django.http import JsonResponse, HttpResponseServerError
from .models import City
import random
import logging

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'index.html')

def random_city(request):
    try:
        all_cities = City.objects.all()
        if not all_cities:
            logger.error("No cities found in the database.")
            return HttpResponseServerError("No cities found.")
        city = random.choice(all_cities)
        return JsonResponse({
            'name': city.name,
            'country': city.country,
            'specialization': city.specialization
        })
    except Exception as e:
        logger.error(f"Error fetching random city: {e}")
        return HttpResponseServerError("An error occurred.")
