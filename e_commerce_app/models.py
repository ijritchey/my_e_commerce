from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.IntegerField(null=True)
    number_remaining = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
