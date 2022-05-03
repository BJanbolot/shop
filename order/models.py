from django.db import models

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey('account.MyUser', on_delete=models.CASCADE, related_name='orders')

