from django.db import models


class Item (models.Model):
    itemName= models.CharField(max_length=20)
    itemPrice = models.IntegerField()
    itemCategory = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.itemName