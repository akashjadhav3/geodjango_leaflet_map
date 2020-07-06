from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from .models import Cities

admin.site.register(Cities, LeafletGeoAdmin)