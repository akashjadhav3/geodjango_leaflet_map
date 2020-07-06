from django.shortcuts import render
from .models import Cities
from django.core.serializers import serialize
from django.http import HttpResponse
import json
import requests

def cities_data(request):
    cities_as_geojson=serialize('geojson', Cities.objects.all())
    return HttpResponse(cities_as_geojson, content_type='json')


def forcast_data(request):
    cities_as_geojson = serialize('geojson', Cities.objects.all())
    data_load_in_json = json.loads(cities_as_geojson)
    cities_with_lat_long = []
    if data_load_in_json:
        for data_row in data_load_in_json["features"]:
            city = data_row["properties"]["name"]
            long_lat = data_row["geometry"]["coordinates"]
            long_lat = str(long_lat[1])+","+str(long_lat[0])
            get_data_requests = requests.get('https://api.weather.gov/points/{}'.format(long_lat))
            weather_details = json.loads(get_data_requests.content)
            forcast_url = weather_details['properties']['forecast']
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', }
            get_forcast_details = requests.get(forcast_url,headers=headers)
            if get_forcast_details.status_code == 200:
                forcast_data = json.loads(get_forcast_details.content)
                forcast_details = forcast_data['properties']['periods'][0]
                temperature = forcast_details['temperature']
                data_dict = {"city":city,"lat_log":long_lat,"temperature":temperature}
                cities_with_lat_long.append(data_dict)
    return HttpResponse(json.dumps(cities_with_lat_long))
