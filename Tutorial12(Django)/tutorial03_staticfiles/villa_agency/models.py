from django.db import models


# Create your models here.

class Product:
    id: int
    name: str
    img: str
    desc: str
    price: int
    dis: int
    dis_price = int
