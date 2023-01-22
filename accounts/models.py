from django.db import models

import uuid
# Create your models here.


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=200, null=True)
    phone = models.BigIntegerField(null=True)
    email = models.EmailField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str((self.name,self.id))

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('In door' , 'In door'),
        ('Out door', 'Out door')
    )
    
    name= models.CharField(max_length=200, null=True)
    price= models.FloatField(max_length=200, null=True)
    category= models.CharField(max_length=200, null=True, choices=CATEGORY)
    description= models.CharField(max_length=200, null=True, blank=True)
    date_created= models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.name

    
class Order (models.Model):
    STATUS = (
        ('Pending' , 'Pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered' , 'Delivered')
    )
    
    customer= models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product= models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add = True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    
    def __str__(self):
        return self.status