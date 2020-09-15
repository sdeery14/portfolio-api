from django.contrib import admin
from .models import SensorReading

# Register your models here.

class SensorReadingAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified', 'taken', 'temp', 'humidity', 'image', )

admin.site.register(SensorReading, SensorReadingAdmin)