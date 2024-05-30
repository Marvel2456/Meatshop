from django.db import models
import uuid

# Create your models here.

class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=250, blank=True, null=True)
    product_image = models.ImageField(upload_to='item/image', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.product_image.url
        except:
            url = ''
        return url
    
class Contact(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=225, blank=True, null=True)
    email = models.CharField(max_length=225, blank=True, null=True)
    phone_number = models.CharField(max_length=225, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.created_at}'

class Branch(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    branch_name = models.CharField(max_length=250, blank=True, null=True)
    branch_address = models.CharField(max_length=250, blank=True, null=True)
    branch_image =  models.ImageField(upload_to='branch/image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.branch_name

