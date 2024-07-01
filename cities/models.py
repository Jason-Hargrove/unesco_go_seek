from django.db import models

# Define the City model
class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    specialization = models.CharField(max_length=200)

    def __str__(self):
        return self.name