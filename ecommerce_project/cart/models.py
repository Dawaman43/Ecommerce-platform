from django.db import models
from products.models import Product
from accounts.models import CustomUser

class Cart(models.Model):
    user = models.OneToOneField(CustomUser, related_name='cart', on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f'Cart for {self.user.username}'

    @property
    def total_price(self):
        return sum(item.product.price * item.quantity for item in self.cart_items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='cart_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.product.name} in {self.cart.user.username}\'s cart'