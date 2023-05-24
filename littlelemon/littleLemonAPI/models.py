from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.category_name


class Menu_Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_ingridiants = models.CharField(max_length=500)
    item_price = models.IntegerField()
    image = models.ImageField(upload_to='images', null=True)
    category_id = models.ForeignKey(
        Category, related_name="category", on_delete= models.CASCADE, default=None
    ) 
    inventory = models.SmallIntegerField()   

    def __str__(self) -> str:
        return self.item_name
    