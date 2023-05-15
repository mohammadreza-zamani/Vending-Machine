from django.db import models

class Machine(models.Model):

    STATUS_IDLE = "idle"
    STATUS_WAITING = "waiting"
    STATUS_ALL = [
        (STATUS_IDLE, "idle"),
        (STATUS_WAITING, "waiting")
    ]

    name = models.CharField(max_length = 50)
    status = models.CharField(blank = False, choices = STATUS_ALL, max_length = 10, default = STATUS_IDLE)
  
class Product(models.Model):
    name = models.CharField(max_length = 50)
    
class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    
    class Meta:
        unique_together = ('product', 'machine',)
    
    
