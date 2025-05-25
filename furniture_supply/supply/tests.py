from django.test import TestCase
from django.urls import reverse
from .models import SupplyOrder, Product, Supplier
from .views import SupplyOrderForm
from django.utils import timezone

class ProductModelTest(TestCase):
    def test_create_product(self):
        product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=10.5,
            stock_quantity=10
        )
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.description, "Test Description")
        self.assertEqual(product.price, 10.5)
        self.assertEqual(product.stock_quantity, 10)

class SupplierModelTest(TestCase):
    def test_create_supplier(self):
        supplier = Supplier.objects.create(
            name="Test Supplier",
            contact_info="test@example.com"
        )
        self.assertEqual(supplier.name, "Test Supplier")
        self.assertEqual(supplier.contact_info, "test@example.com")

class SupplyOrderModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=10.5,
            stock_quantity=10
        )
        self.supplier = Supplier.objects.create(
            name="Test Supplier",
            contact_info="test@example.com"
        )

    def test_create_order(self):
        order = SupplyOrder.objects.create(
            product=self.product,
            supplier=self.supplier,
            quantity=10,
            status='waiting',
            order_date=timezone.now()
        )
        self.assertEqual(order.product, self.product)
        self.assertEqual(order.supplier, self.supplier)
        self.assertEqual(order.quantity, 10)
        self.assertEqual(order.status, 'waiting')

class SupplyOrderFormTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=10.5,
            stock_quantity=10
        )
        self.supplier = Supplier.objects.create(
            name="Test Supplier",
            contact_info="test@example.com"
        )

    def test_valid_form(self):
        data = {
            'product': self.product.id,
            'supplier': self.supplier.id,
            'quantity': 5,
            'status': 'waiting'
        }
        form = SupplyOrderForm(data=data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())

