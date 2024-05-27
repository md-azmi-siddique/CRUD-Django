from rest_framework import serializers
from .models import * # Ensure this imports the correct model

class crudSerializer(serializers.ModelSerializer):
    class Meta:
        model = crudModel  # Ensure this points to the correct model
        fields = '__all__'  # or specify the fields explicitly
