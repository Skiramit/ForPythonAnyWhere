from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Country(models.Model):
    country_name = models.CharField(max_length = 100)
    country_code = models.CharField(max_length = 3)


    def __str__(self):
        return self.country_name


class Part(models.Model):
    part_name = models.CharField(max_length = 50)
    part_price = models.IntegerField()
    part_car = models.CharField(max_length = 50)


    def __str__(self):
        return self.part_name


class Car(models.Model):
    car_name = models.CharField(max_length = 50)
    car_color = models.CharField(max_length = 50)
    car_year = models.IntegerField()
    country = models.ForeignKey(Country, on_delete = models.CASCADE)
    part = models.ManyToManyField(Part)


    def __str__(self):
        return self.car_name 
