from django.db import models

# Create your models here.
class Product(models.Model):
    Image = models.ImageField(upload_to='product_image',null=True)
    title = models.CharField(max_length=100, primary_key=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.price}'

