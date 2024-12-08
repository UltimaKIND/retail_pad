from django.db import models

NULLABLE = {'null': True, 'blank': True}

class Node(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='поставщик', **NULLABLE)
    duty_supp = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='задолженность', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='email')
    country = models.CharField(max_length=100, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город')
    street = models.CharField(max_length=100, verbose_name='улица')
    house = models.CharField(max_length=100, verbose_name='номер дома')

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    node = models.ManyToManyField(Node, related_name='products')
    name = models.CharField(max_length=100, verbose_name='название')
    model = models.CharField(max_length=100, verbose_name='модель')
    market_entry_date = models.DateField(**NULLABLE)

    def __str__(self):
        return f'{self.name} {self.model}'