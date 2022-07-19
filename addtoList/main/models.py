from django.db import models
from django.conf import settings
# Create your models here.


class Grocery(models.Model):
    #The main Grocery list model
    
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    bought = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name="Grocery")

    class Meta:
        #Meta Information
        verbose_name = "Grocery"
        verbose_name_plural = "Groceries"
    def __str__(self):
        return self.name

class GroceryItem(models.Model):
    quantity = models.IntegerField()
    price =  models.IntegerField()