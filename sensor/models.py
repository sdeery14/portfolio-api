from django.db import models

# Create your models here.

class SensorReading(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	taken = models.DateTimeField()
	temp = models.FloatField()
	humidity = models.FloatField()
	image = models.ImageField(upload_to='post_images')