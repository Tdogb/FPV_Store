from django.db import models
import datetime

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    date_released = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    in_stock = models.BooleanField()
    description = models.TextField()
    thumb = models.ImageField(default='/media/default.png')

    def __str__(self):
        return self.name