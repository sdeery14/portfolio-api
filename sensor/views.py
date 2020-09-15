from .models import SensorReading
from .serializers import SensorReadingSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

class SensorReadingViewSet(ModelViewSet):
    queryset = SensorReading.objects.all()
    serializer_class = SensorReadingSerializer

class LatestSensorReadingRetrieveView(APIView):
	def get(self, request):
		queryset = SensorReading.objects.latest('taken')
		serializer_class = SensorReadingSerializer(queryset, context={'request': request})
		return Response(serializer_class.data)