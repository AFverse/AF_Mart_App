from django.db import models
from authentication.models import *
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import uuid
User = get_user_model()

class ParentCategory(models.Model):
    name = models.CharField(max_length=100)
    disc = models.TextField()
    img = models.ImageField(upload_to='parentCategory/images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    disc = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='categories/images')
    parent_category = models.ForeignKey(ParentCategory, null=True, blank=True, on_delete=models.CASCADE, related_name='subCat')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name
    

class Product(models.Model):
    title = models.CharField(max_length=100)
    disc = models.TextField(null=True, blank=True)
    slug = models.SlugField()
    SKU = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.ImageField(upload_to='product_images')
    discount = models.ForeignKey('Discount', on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    inventory = models.PositiveIntegerField(null=True, blank=True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    has_variations = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    top_selling = models.BooleanField(default=False)
    is_recommended = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    def get_discounted_price(self):
        if self.discount:
            discount_amount = (self.discount.percentage / 100) * self.price
            discounted_price = self.price - discount_amount
            discounted_price = int(discounted_price)
            return round(discounted_price, 2)
        else:
            return self.price




# class VariationManager(models.Manager):
#     def flavor(self):
#         return super(VariationManager, self).filter(variation_category='flavor', is_active=True)
    
#     def sizes(self):
#         return super(VariationManager, self).filter(variation_category='size', is_active=True)



# variation_category_choice = (
#     ('flavor', 'flavor'),
#     ('size', 'size'),  
# )

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.ForeignKey('VeriationsCategory', on_delete=models.CASCADE, null=True, blank=True)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=0)

    # objects = VariationManager()
    
    def __str__(self):
        return self.variation_category.name
    
class VeriationsCategory(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name


class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='reviews')
    rating = models.FloatField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')

    
    
class Discount(models.Model):
    name = models.CharField(max_length=100)
    disc = models.TextField()
    percentage = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str: 
        return f'{self.percentage} on{self.name}'
    
class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name






class CartItmes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderItems(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    
    STATUS_OPTIONS = [
        ('cart', 'CART'),
        ('pending', 'PENDING'),
        ('completed', 'COMPLETED')
    ]
    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_OPTIONS, default='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
class UserItem(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    is_in_cart = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



