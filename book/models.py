from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    pages = models.CharField(max_length=3)
    price = models.DecimalField(max_digits=5, decimal_places=2)