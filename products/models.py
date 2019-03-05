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
    S800 = 's800'
    GEN = 'general'
    PRODUCT_TYPES = (
        (S800, 's800'),
        (GEN, 'general'),
    )
    product_type = models.CharField(default=GEN, choices=PRODUCT_TYPES, max_length=50)

    def getProductTypes(self):
        return self.PRODUCT_TYPES

    def __str__(self):
        return self.name