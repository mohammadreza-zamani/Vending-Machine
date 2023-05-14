from django.db import models

class Machine(models.Model):
    name = models.CharField(max_length = 50)
    status = models.TextChoices("status", "idle waiting")
  
class Product(models.Model):
    name = models.CharField(max_length = 50)
    
class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    machine = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    
    
  
