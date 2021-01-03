from django.urls import path, include
from .views import ListingAPIView, ListingDetails, CreateListing, ListingOptions

urlpatterns = [
    path('api/listings', ListingAPIView.as_view()),
    path('api/listing/<int:id>', ListingDetails.as_view()),
    path('api/listing-create', CreateListing.as_view()),
    path('api/listing-options/<int:id>', ListingOptions.as_view()),
]