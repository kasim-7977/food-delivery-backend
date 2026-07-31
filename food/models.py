from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="categories/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="foods"
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="foods/")
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    full_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    status = models.CharField(max_length=20,default="Pending")
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    def __str__(self):
        return f"Order #{self.id} - {self.full_name}"
        
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField()

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.food.name} x {self.quantity}"

    # def __str__(self):
    #     return self.full_name

    # def __str__(self):
    #     return self.name
