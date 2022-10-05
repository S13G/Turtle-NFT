from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(default='default.png', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='products')
    token = models.CharField(max_length=100, null=True, blank=True, default="TTC")
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(1)])
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name