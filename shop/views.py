from django.shortcuts import render,redirect
from .models import shop_model
from cars.models import car

# Create your views here.
def byNow (request, id):
    author = request.user
    product_id = id
    product = car.objects.get(pk = product_id)
    purchase = shop_model.objects.create(author_name=author, product_id=product_id)
    product.quantity = str(int(product.quantity) - 1)
    product.save()
    return redirect("car_bye", id = product_id)