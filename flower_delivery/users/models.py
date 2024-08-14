from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    email = models.EmailField(max_length=254, unique=True)
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'
