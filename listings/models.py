from datetime import datetime
import arrow
from django.db import models
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Listing(models.Model):
    coordinates = models.CharField(max_length=200, null=True)
    date = models.CharField(max_length=200, null=True)
    diachibds = models.CharField(max_length=200, null=True)
    dientich = models.CharField(max_length=200, null=True)
    dtsd = models.CharField(max_length=200, null=True)
    feature = models.TextField(null=True)
    geocoded = models.CharField(max_length=20, null=True)
    gia = models.CharField(max_length=200, null=True)
    image_uri = models.CharField(max_length=200, null=True)
    khuvuc = models.CharField(max_length=200, null=True)
    lat = models.CharField(max_length=200, null=True)
    lienhe = models.CharField(max_length=200, null=True)
    loaitinrao = models.CharField(max_length=200, null=True)
    long = models.CharField(max_length=200, null=True)
    mota = models.TextField(null=True)
    mobile = models.BigIntegerField(null=True)
    
    name = models.CharField(max_length=200, null=True)
    #first_name = models.CharField(_("First name"), max_length=255)
    name_unidecode = models.CharField(max_length=200, null=True)
    ngaydang = models.CharField(max_length=200, null=True)
    phongngu = models.CharField(max_length=200, null=True)
    phongtam = models.CharField(max_length=200, null=True)
    project = models.CharField(max_length=200, null=True)
    server = models.CharField(max_length=200, null=True)
    spider = models.CharField(max_length=200, null=True)
    tang = models.CharField(max_length=200, null=True)
    tieude = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    acreage = models.CharField(max_length=200, null=True)
    internal_roads = models.CharField(max_length=200, null=True)
    hxh = models.CharField(max_length=200, null=True)
    hemxehoi = models.CharField(max_length=200, null=True)
    area = models.CharField(max_length=200, null=True)
    house_width = models.CharField(max_length=200, null=True)
    bedrooms = models.IntegerField(null=True)
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    floors = models.CharField(max_length=200, null=True)
    ground_floor = models.CharField(max_length=200, null=True)
    terraces = models.CharField(max_length=200, null=True)
    predict = models.CharField(max_length=200, null=True)
    is_published = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    # def __str__(self):
    # return self.khuVuc
