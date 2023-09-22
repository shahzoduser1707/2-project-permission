from rest_framework import serializers
from .models import PhoneModel

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneModel
        fields = ('__all__')