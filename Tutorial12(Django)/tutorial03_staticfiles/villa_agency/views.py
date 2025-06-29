from django.shortcuts import render

from .models import Product


# Create your views here.

def home(request):
    product = Product()
    product.name = "Iphone 6S"
    product.img = "https://i.guim.co.uk/img/media/ac8cc7193827bc8e5a1ec338113c49ea21248174/0_0_2100_1260/master/2100.jpg?width=445&dpr=1&s=none&crop=none"
    product.desc = "Available offers\nBank Offer100% Cashback upto 500Rs on Axis Bank SuperMoney Rupay CC UPI transactions on super.money UPIT&C\nBank Offer5% cashback on Flipkart Axis Bank Credit Card upto ₹4,000 per statement quarterT&C"
    product.price = 44
    product.dis = 0
    product.dis_price = product.price - product.dis

    product1 = Product()
    product1.name = "Samsung S23"
    product1.img = "https://m.media-amazon.com/images/I/51ygk8oviDL.jpg"
    product1.desc = "Available offers\nBank Offer100% Cashback upto 500Rs on Axis Bank SuperMoney Rupay CC UPI transactions on super.money UPIT&C\nBank Offer5% cashback on Flipkart Axis Bank Credit Card upto ₹4,000 per statement quarterT&C"
    product1.dis = 20
    product1.price = 50
    product1.dis_price = product1.price - product1.dis

    products = [product, product1]

    return render(request, "index.html", {"products": products})


def productdetail(request):
    return render(request, "product-detail.html")


def products(request):
    return render(request, "products.html")


def cart(request):
    return render(request, "cart.html")


def checkout(request):
    return render(request, "checkout.html")
