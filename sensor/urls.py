from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SensorReadingViewSet, LatestSensorReadingRetrieveView
from django.conf.urls.static import static
from django.conf import settings

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'sensor_readings', SensorReadingViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('latest_sensor_reading/', LatestSensorReadingRetrieveView.as_view(), name="latest_sensor_reading"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)