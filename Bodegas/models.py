from django.db import models
from datetime import datetime

# Create your models here.
CHOICES = (
    ('------','------'),
    ('bodega','BODEGA'),
    ('terreno','TERRENO'),
)

STATE_CHOICES = (
    ('------','------'),
    ('GDL','Guadalajara'),
    ('ZAP','Zapopan'),
    ('TLJ','Tlajomulco'),
    ('TNL','Tonala'),
    ('CHA','Chapala'),
    ('STL','El Salto'),
)

TRANSACTION_CHOICES = (
    ('------','------'),
    ('RNT','RENTA'),
    ('VNT','VENTA'),
)

class Listing(models.Model):
  property_type = models.CharField(max_length=50, choices=CHOICES, default='------')
  transaction_type = models.CharField(max_length=50, choices=TRANSACTION_CHOICES, default='------')
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100, choices=STATE_CHOICES, default='------')
  zipcode = models.CharField(max_length=20)
  description = models.TextField(blank=True)
  price = models.IntegerField()
  sqft = models.IntegerField()
  lot_size = models.DecimalField(max_digits=5, decimal_places=1)
  is_published = models.BooleanField(default=True)
  office = models.BooleanField(default=False)
  dock = models.BooleanField(default=False)
  industrial_park = models.BooleanField(default=False)
  vigilancia = models.BooleanField(default=False)
  parking = models.BooleanField(default=False)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.title