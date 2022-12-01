from django.db import models
from datetime import date

class Wish(models.Model):
    image = models.URLField(blank=False, null=False)
    product_name = models.CharField(max_length=50, blank=False, null=False)
    price = models.FloatField(default=0)
    stock = models.BooleanField(default=False)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.product_name

