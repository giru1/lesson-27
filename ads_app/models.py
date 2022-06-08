from django.db import models


# Create your models here.

class Ads(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name