from django.shortcuts import render
from .models import Cities
from django.core.serializers import serialize
from django.http import HttpResponse
import json
import requests

def cities_data(request):
    cities_as_geojson=serialize('geojson', Cities.objects.all())
    a = json.loads(cities_as_geojson)
    cities_with_lat_long = []
    for i in a["features"]:
        city = i["properties"]["name"]
        long_lat = i["geometry"]["coordinates"]
        long_lat = str(long_lat[1])+","+str(long_lat[0])
        get_data_requests = requests.get('https://api.weather.gov/points/{}'.format(long_lat))
        weather_details = json.loads(get_data_requests.content)
        forcast_url = weather_details['properties']['forecast']
        print(forcast_url)
        get_forcast_details = requests.get(forcast_url)
        forcast_data = json.loads(get_forcast_details.content)
        forcast_details = forcast_data['properties']['periods'][0]
        temperature = forcast_details['temperature']
        temperatureUnit = forcast_details['temperatureUnit']
        icon = forcast_details['icon']
        shortForecast = forcast_details['shortForecast']
        detailedForecast = forcast_details['detailedForecast']
        data_dict = {"city":city,"lat_log":long_lat,"temperature":temperature,"temperatureUnit":temperatureUnit,"icon":icon,
                    "shortForecast":shortForecast,"detailedForecast":detailedForecast}
        cities_with_lat_long.append(data_dict)
    # context = { "weather_data":cities_with_lat_long,"map_data":cities_as_geojson}

    return HttpResponse(cities_as_geojson, content_type='json')