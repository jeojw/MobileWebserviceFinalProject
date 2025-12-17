from rest_framework import serializers
from .models import ChangeImage

class ChangeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChangeImage
        fields = '__all__'
