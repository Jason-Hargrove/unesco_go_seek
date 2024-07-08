import csv
from django.core.management.base import BaseCommand
from cities.models import City

class Command(BaseCommand):
    help = 'Load initial data into the cities table'

    def handle(self, *args, **kwargs):
        with open('cities_data.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                City.objects.create(
                    name=row['name'],
                    country=row['country'],
                    specialization=row['specialization']
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded city data'))
