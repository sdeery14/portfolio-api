from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import SensorReading

class SensorReadingSerializer(ModelSerializer):
    class Meta:
        model = SensorReading
        fields = '__all__'