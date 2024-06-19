# Setup of viewset for 'stock' model (RESTful API endpoint for CRUD operations)

from django.shortcuts import render
from rest_framework import viewsets
from .models import stock
from .serializers import StockSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = stock.objects.all()
    serializer_class = StockSerializer
    
#ModelViewSet (is by DRF) provides default implementations for CRUD operations

# defines the queryset and retrieves all 'stock' objects from the db

# serializer_class - specifices to serialize and deserialize 'stock' objects 