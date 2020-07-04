from django.shortcuts import render
from .models import Cities
from django.core.serializers import serialize
from django.http import HttpResponse

def cities_data(request):
    cities_as_geojson=serialize('geojson', Cities.objects.all())
    return HttpResponse(cities_as_geojson, content_type='json')