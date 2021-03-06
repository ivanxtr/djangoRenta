from django.urls import path, include
from .views import ListingAPIView, ShopAPIView, LocaleAPIView, ListingDetails, CreateListing, ListingOptions, GetListingsCount, GetShopCount, GetLocaleCount

urlpatterns = [
    path('api/listings', ListingAPIView.as_view()),
    path('api/shop', ShopAPIView.as_view()),
    path('api/locale', LocaleAPIView.as_view()),
    path('api/listing/<int:id>', ListingDetails.as_view()),
    path('api/listing-create', CreateListing.as_view()),
    path('api/listing-options/<int:id>', ListingOptions.as_view()),
    path('api/count', GetListingsCount.as_view()),
    path('api/shop-count', GetShopCount.as_view()),
    path('api/locale-count', GetLocaleCount.as_view())
]
