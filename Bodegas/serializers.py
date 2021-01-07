from rest_framework import serializers
from .models import Listing

class ListingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['property_type', 'transaction_type', 'title', 'address', 'city', 'state', 'zipcode', 'description', 'price', 'sqft', 'lot_size', 'office', 'dock', 'industrial_park', 'vigilancia', 'parking', 'photo_main', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6', 'list_date']

class ListingsSerialiers(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['transaction_type', 'price', 'sqft', 'lot_size', 'office', 'dock', 'industrial_park', 'vigilancia', 'parking', 'address', 'photo_1']