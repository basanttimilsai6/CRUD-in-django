from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Student(models.Model):
    sid = models.CharField(max_length=4)
    sname = models.CharField(max_length=255)
    scontact = models.CharField(max_length=15)

    def __str__(self):
        return self.sname