from django.test import TestCase
from products.models import Product
from products.models import ProductType
from products.models import Orders
from django.contrib.auth.models import User


class ProductTestCase(TestCase):
	def setUp(self):
		Product.objects.create(name="lego", price=100, description="ultimate lego set", quantity=2, customer_id=0, product_type_id=0)
		Product.objects.create(name="jigsaw puzzle", price=30, description="1000 piece puzzle", quantity=3, customer_id=1, product_type_id=1)

	def test_product_has_lego(self):
		lego = Product.objects.get(name='lego')
		self.assertEqual(lego.price, 100)
		self.assertEqual(lego.description, 'ultimate lego set')

	def test_product_has_jigsaw_puzzle(self):
		jigsaw_puzzle = Product.objects.get(name='jigsaw puzzle')
		self.assertEqual(jigsaw_puzzle.price, 30)
		self.assertEqual(jigsaw_puzzle.quantity, 3)

class ProductTypeTestCase(TestCase):
	def setUp(self):
		ProductType.objects.create(label ="electronics")

	def test_product_type_has_electronics(self):
		electronics = ProductType.objects.get(label='electronics')
		self.assertEqual(electronics.label, "electronics")


# class OrdersTestCase(TestCase):
# 	def setUp(self):
# 		Orders.objects.create(active=True, created=True, customer=User_id, payment_type=1, product=1)

# 	def test_orders_have_product(self):
# 		orders = Orders.objects,get(product=1)
# 		self.assertEqual(orders.product, 1)