from django.contrib import admin

# Register your models here.

from .models import Country, Part, Car

admin.site.register(Country)
admin.site.register(Part)
admin.site.register(Car)