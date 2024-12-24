from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.TextField("Название товара", max_length=200)
    description = models.TextField("описание товара")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
