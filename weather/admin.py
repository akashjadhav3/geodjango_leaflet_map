from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from .models import Cities

class CitiesAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location') # user for show column name

admin.site.register(Cities, CitiesAdmin)