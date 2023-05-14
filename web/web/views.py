from django.shortcuts import render
from django.http import HttpResponse
from .models import Machine, Product, Variant

def reset(request):
    Machine.objects.all().delete()
    Product.objects.all().delete()
    Variant.objects.all().delete()
    
    machine1 = Machine(id = 1, name = "machine1", status = "idle")
    machine1.save()
    machine2 = Machine(id = 2, name = "machine2", status = "idle")
    machine2.save()
    
    product1 = Product(id = 1, name = "coffee")
    product1.save()
    product2 = Product(id = 2, name = "juice")
    product2.save()
    
    variant1 = Variant(id = 1, product = 1, machine = 1, quantity = 7)
    variant1.save()
    variant2 = Variant(id = 2, product = 2, machine = 1, quantity = 5)
    variant2.save()
    variant3 = Variant(id = 3, product = 1, machine = 2, quantity = 8)
    variant3.save()
    variant4 = Variant(id = 4, product = 2, machine = 2, quantity = 9)
    variant4.save()
    
    return HttpResponse("Done")

def machines(request):
    return HttpResponse("Hello world!")

