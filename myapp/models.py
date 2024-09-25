from django.db import models # type: ignore

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    pic = models.ImageField(upload_to="products/", null=True)
    
    def __str__(self):
        return self.name 

