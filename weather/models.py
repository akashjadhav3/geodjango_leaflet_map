from django.db import models
from djgeojson.fields import PointField
from django.db.models import Manager as GeoManager
from django.contrib.gis.db import models as gismodel

class Cities(models.Model):
    name = models.CharField(max_length=20)
    location = gismodel.PointField(srid=4326)
    objects = GeoManager()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'cities'