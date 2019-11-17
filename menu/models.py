from django.db import models


class Menu(models.Model):
    menu_name = models.CharField(max_length=100)
    store_name = models.CharField(max_length=100)
    price = models.IntegerField(null=False)

    def __str__(self):
        return self.menu_name


class Store(models.Model):
    store_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200, default="")
    tel = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.store_name



