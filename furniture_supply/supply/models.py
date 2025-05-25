from django.db import models

from django.db import models

class Product(models.Model):
    name = models.CharField('Название товара', max_length=100)
    description = models.TextField('Описание', blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField('Количество на складе', default=0)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField('Поставщик', max_length=100)
    contact_info = models.CharField('Контактная информация', max_length=200, blank=True)

    def __str__(self):
        return self.name

class SupplyOrder(models.Model):
    STATUS_CHOICES = [
        ('waiting', 'Ожидает'),
        ('delivered', 'Доставлено'),
        ('cancelled', 'Отменено'),
    ]

    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, verbose_name='Поставщик', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Количество')
    status = models.CharField('Статус', max_length=10, choices=STATUS_CHOICES, default='waiting')
    order_date = models.DateField('Дата заказа', auto_now_add=True)

    def __str__(self):
        return f'{self.product.name} от {self.supplier.name} — {self.status}'
