from django.db import models
from accounts.models import Flags

# Create your models here.

class Event(models.Model):
    name =  models.CharField(max_length=30)
    flags = models.ManyToManyField(Flags)