from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='catalog/img/')
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


