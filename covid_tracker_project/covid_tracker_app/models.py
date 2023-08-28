from django.db import models

class DataEntry(models.Model):
    date = models.DateField()
    country = models.CharField(max_length=100)
    c_cases = models.PositiveIntegerField()
    c_deaths = models.PositiveIntegerField()

    def __str__(self):
        return self.country
