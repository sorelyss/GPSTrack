from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Data(models.Model):
	longitude = models.CharField(max_length=30)
	latitude = models.CharField(max_length=30)
	date = models.DateTimeField(max_length=30)