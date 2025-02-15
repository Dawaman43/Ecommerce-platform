from django.db import models
from accounts.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name='products')
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    seller = models.ForeignKey(CustomUser, related_name='seller_products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product_Review(models.Model):
    product = models.ForeignKey(Product, related_name='product_reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='user_product_reviews', on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} on {self.product.name}'