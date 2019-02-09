from django.db import models
from django.utils import timezone


class Hpux(models.Model):
    servername = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, blank=True)
    date = models.DateField(default=timezone.now)
    patch_bundle = models.CharField(max_length=100)
