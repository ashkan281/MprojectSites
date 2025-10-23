from django.db import models

# Create your models here.


class change_icon(models.Model):
    images = models.ImageField(upload_to="images")
    number = models.IntegerField()
    description = models.CharField(max_length=25)
    
    def __str__(self):
        return self.description