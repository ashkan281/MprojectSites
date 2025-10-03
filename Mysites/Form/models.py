from django.db import models

# Create your models here.


class message(models.Model):
    name = models.CharField(max_length=10)
    namefamily = models.CharField(max_length=10)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    sub = models.CharField()
    
    
    
    def __str__(self):
        return f"{self.name}  {self.namefamily}"
    
    