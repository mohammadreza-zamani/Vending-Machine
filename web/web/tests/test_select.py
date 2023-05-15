
from django.test import TestCase
from web.models import Machine, Variant, Product
from django.urls import reverse

class SelectTestCase(TestCase):
    def setUp(self):
        self.quantity = 7
        machine1 = Machine(id = 1, name = "machine1", status = Machine.STATUS_WAITING)
        machine1.save()

        product1 = Product(id = 1, name = "coffee")
        product1.save()

        variant = Variant(id = 1, product = product1, machine = machine1, quantity = self.quantity)
        variant.save()

    def test_select(self):
        variant = Variant.objects.get(id = 1)
        self.client.get(reverse('select', args = (variant.id,)))
        variant = Variant.objects.get(id = 1)
        machine = variant.machine
        self.assertEqual(variant.quantity, self.quantity - 1)
        self.assertEqual(machine.status, Machine.STATUS_IDLE)

