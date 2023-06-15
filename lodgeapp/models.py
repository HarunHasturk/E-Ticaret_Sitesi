from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.IntegerField(primary_key = True)
    product_name = models.CharField(max_length=255)
    product_image = models.ImageField(upload_to='lodgeapp/static/images/')
    product_price = models.CharField(max_length=255)
    product_url = models.URLField(blank=True)

class Slider(models.Model):
    slider_id = models.IntegerField(primary_key=True)
    slider_collection = models.CharField(max_length=255)
    slider_title = models.CharField(max_length=255)
    slider_content = models.TextField()
    slider_url = models.URLField(blank=True)
    slider_image = models.ImageField(upload_to='lodgeapp/static/images/')

class BestPrices(models.Model):
    price_id = models.IntegerField(primary_key=True)
    price_assessment = models.CharField(max_length=255)
    price_image = models.ImageField(upload_to='lodgeapp/static/images/')
    price_name = models.CharField(max_length=255)

class About(models.Model):
    about_title = models.CharField(max_length=255)
    about_content = models.TextField()
    about_url = models.URLField(blank=True)
    about_image = models.ImageField(upload_to='lodgeapp/static/images/')

class Special(models.Model):
    special_title = models.CharField(max_length=255)
    special_url = models.URLField(blank=True)
    special_image = models.ImageField(upload_to='lodgeapp/static/images/')

class Testimonial(models.Model):
    testimonial_id = models.IntegerField(primary_key=True)
    testimonial_image = models.ImageField(upload_to='lodgeapp/static/images/')
    testimonial_name = models.CharField(max_length=255)
    testimonial_recommendation = models.CharField(max_length=255)
    testimonial_content = models.TextField()

class Cart(models.Model):
    cart_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(null=True)

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
