from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DogSerializer, BreedSerializer
from .models import Dog, Breed
# Create your views here.

class DogView(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

class BreedView(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
