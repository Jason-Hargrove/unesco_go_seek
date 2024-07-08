import os
import csv
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'unesco_go_seek.settings')
django.setup()

from cities.models import City

with open('cities_data.csv', newline='') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    for row in reader:
        name, country, specialization = row
        City.objects.create(name=name, country=country, specialization=specialization)

print("Data loaded successfully!")