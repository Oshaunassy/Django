from django.db import models


# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to='media', null=True)
    title = models.CharField(max_length=100, primary_key=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.price}'


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'

class Review(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"Review by {self.author} for {self.product.name}"