from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("products", views.products, name="products"),
    path("product-detail", views.productdetail, name="product-detail"),
    path("cart", views.cart, name="cart"),
    path("checkout", views.checkout, name="checkout")
]
