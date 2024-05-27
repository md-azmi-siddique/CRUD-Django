from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.

class crudCreate(generics.CreateAPIView):
    queryset = crudModel.objects.all()
    serializer_class = crudSerializer
    
class crudRead(generics.ListAPIView):
    queryset = crudModel.objects.all()
    serializer_class = crudSerializer

class crudUpdate(generics.RetrieveAPIView):
    queryset = crudModel.objects.all()
    serializer_class = crudSerializer
    
class crudDelete(generics.DestroyAPIView):
    queryset = crudModel.objects.all()
    serializer_class = crudSerializer
    


