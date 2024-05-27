from rest_framework import serializers
from . models import *

class crudSerializer(serializers.ModelSerializer):
    class Meta:
        model = crudModel
        field = '__all__'