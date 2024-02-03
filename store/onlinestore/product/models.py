from django.db import models
class Manufacture(models.Model):
    name=models.CharField(max_length=120)
    location=models.CharField(max_length=120)
    active=models.BooleanField(default=True)
    def __str__(self):
        return  self.name
class Product(models.Model):
    manufacture = models.ForeignKey(Manufacture,
     related_name="product",
     on_delete=models.CASCADE)
    name = models.CharField(max_length = 150)
    price = models.FloatField()
    shipping_cost = models.FloatField()
    photo = models.ImageField(blank=True,null=True)
    quantity = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.name
    
    
    


    
    


    
    
