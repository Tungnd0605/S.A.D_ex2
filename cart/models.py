from django.db import models
from book.models import book
# Create your models here.

class CartItem(models.Model):
    book = models.ForeignKey(book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Order(models.Model):
    items = models.ManyToManyField(CartItem)
    total_price = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
