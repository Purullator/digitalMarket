from django.db import models

# Create your models here.

class Product(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.FloatField()
    file = models.FileField(upload_to='uploads')

    def __str__(self):
        return self.name