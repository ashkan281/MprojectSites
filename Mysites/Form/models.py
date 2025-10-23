from django.db import models
from django.core.validators import RegexValidator
from django import forms
# Create your models here.


class Message(models.Model):
    conName = models.CharField(max_length=10)
    conLName = models.CharField(max_length=10, blank=True, null=True)
    conEmail = models.EmailField(max_length=255)
    conPhone = models.CharField(max_length=15)
    conMessage = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.conName} {self.conLName}"
    
    

