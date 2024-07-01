import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'unesco_go_seek.settings')
django.setup()

from cities.models import City

with open('cities.txt') as f:
    for line in f:
        name, country, specialization = line.strip().split(', ')
        City.objects.create(name=name, country=country, specialization=specialization)

print("Data loaded successfully!")
