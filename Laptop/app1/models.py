from django.db import models

# Create your models here.


class Laptop(models.Model):
    lid = models.IntegerField()
    brand_name = models.CharField(max_length=50)
    price = models.IntegerField()
    rom = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    ssd = models.CharField(max_length=50)
    hdd = models.CharField(max_length=50)
    weight = models.FloatField()
    year = models.IntegerField()


    def __str__(self):
        return f"{self.lid}--{self.brand_name}--{self.price}"