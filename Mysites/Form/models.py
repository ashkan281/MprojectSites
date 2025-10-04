from django.db import models
from django.core.validators import RegexValidator
from django import forms
# Create your models here.


class message(models.Model):
    conName = models.CharField(max_length=10)
    conLName = models.CharField(max_length=10, blank=True, null=True)
    conEmail = models.EmailField()
    conPhone = models.CharField(max_length=15)
    conMessage = models.CharField(max_length=255, null=False, blank=False)
    
    
    
    def __str__(self):
        return self.conName
    
    
