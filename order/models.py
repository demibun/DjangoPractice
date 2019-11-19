from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=50)
    tel = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    menu_name = models.CharField(max_length=100)
    store_name = models.CharField(max_length=100)
