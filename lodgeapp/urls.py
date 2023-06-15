from django.urls import path
from . import views
from django.contrib.auth.models import User

urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index),
    path("about", views.about, name="about"),
    path("jewellery", views.jewellery, name="jewellery"),
    path("contact", views.contact, name="contact"),
    path('add-product/<int:product_id>',views.add_product, name="add_product"),
    path("cart", views.cart, name="cart"),
    path("delete-cart-product/<int:cart_product_id>", views.delete_cart_product, name="delete_cart_product"),
    path("set-cart-product/<int:cart_product_id>", views.set_cart_product_quantity, name="set_cart_product_quantity")
]
