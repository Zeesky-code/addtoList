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
    quantity = models.IntegerField(default = 1)
    price =  models.IntegerField(default = 1)
    note = models.CharField(max_length= 500)
    class Category_choices(models.TextChoices):
        Fruits = '🍓Fruits',
        Vegetables = '🥒Vegetables',
        Canned_Goods = '🥫Canned Goods',
        Dairy = '🥛Dairy',
        Meat = '🥩Meat',
        Seafood = '🐟Fish & Seafood',
        Condiments = '🧂Condiments and Spices',
        Snacks = '🍟Snacks',
        Baked_Goods = '🍞Baked Goods',
        Beverages = '🧃Beverages',
        Pasta_and_Rice = '🍝Pasta',
        Baking_Products = '🥚Baking Products',
        Frozen_Food = '🍗Frozen Food',
        Baby_Items = '🚼Baby Items',
        Pet_Care = '🐕Pet Care',
        Miscellaneous = 'Miscellaneous'


        
    category = models.CharField(max_length = 200,choices = Category_choices.choices, default= "blank")

    class Meta:
        #Meta Information
        verbose_name = "Grocery"
        verbose_name_plural = "Groceries"
    def __str__(self):
        return self.name

