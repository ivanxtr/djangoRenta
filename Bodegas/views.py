from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Listing
from .serializers import ListingSerializers

class ListingAPIView(APIView):
  def get(self, request):
    Listings = Listing.objects.all()
    serializer = ListingSerializers(Listings, many=True)
    return Response(serializer.data)

class ListingDetails(APIView):
  def get_object(self, id):
    try:
      return Listing.objects.get(id=id)
    except Listing.DoesNotExist:
      return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
  def get(self, request, id):
    Listing = self.get_object(id)
    serializer = ListingSerializers(Listing)
    return Response(serializer.data)

class CreateListing(APIView):
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticated]
    
  def post(self, request):
    serializer = ListingSerializers(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListingOptions(APIView):
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticated]
  
  def get_object(self, id):
    try:
      return Listing.objects.get(id=id)
    except Listing.DoesNotExist:
      return HttpResponse(status=status.HTTP_404_NOT_FOUND)

  def put(self, request, id):
    Listing = self.get_object(id)
    serializer = ListingSerializers(Listing, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, id):
    Listing = self.get_object(id)
    Listing.delete()
    return HttpResponse(status=status.HTTP_204_NO_CONTENT)  