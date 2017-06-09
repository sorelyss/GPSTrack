#from __future__ import unicode_literals
from django.db import models

class Data(models.Model):
	device = models.CharField(max_length=30, default='syrus')
	longitude = models.CharField(max_length=30)
	latitude = models.CharField(max_length=30)
	elevation = models.CharField(max_length=30)
	date = models.DateTimeField(max_length=30)
