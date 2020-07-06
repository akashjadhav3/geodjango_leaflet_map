from django.urls import path
from django.conf import settings
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('data/',views.cities_data, name='data'),
    path('forcast/',views.forcast_data, name='forcast_data')
]