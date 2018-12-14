from django.db import models

# Create your models here.

class Ise(models.Model):
	iseIP = models.GenericIPAddressField(default='', blank=False, null=False)
	iseUname = models.CharField(max_length=20, default='', blank=True)
	isePWord = models.CharField(max_length=30, default='', blank=True)


