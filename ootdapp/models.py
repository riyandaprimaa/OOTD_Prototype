from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True)
    #age = models.IntegerField(blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


class Product(models.Model):
    ProductID = models.IntegerField()
    Gender = models.CharField()
    Category = models.CharField()
    SubCategory = models.CharField()
    ProductType = models.CharField()
    Colour = models.CharField()
    Usage = models.CharField()
    ProductTitle = models.CharField()
    Image = models.ImageField()
    ImageURL = models.CharField()

    def __str__(self):
        return self.ProductID
