from django.test import TestCase
from web.models import Machine
from django.urls import reverse

class BuyTestCase(TestCase):
    def setUp(self):
        Machine.objects.create(name = "machine1", status = Machine.STATUS_IDLE)

    def test_buy(self):
        machine = Machine.objects.get(name="machine1")
        self.client.get(reverse('buy', args = (machine.id,)))
        machine = Machine.objects.get(name="machine1")
        self.assertEqual(machine.status, Machine.STATUS_WAITING)
