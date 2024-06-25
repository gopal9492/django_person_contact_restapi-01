from rest_framework import serializers
from .models import contacts


class contactSerializers(serializers.ModelSerializer):
    class Meta:
        model = contacts
        fields = '__all__'
