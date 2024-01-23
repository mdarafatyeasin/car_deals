from django.shortcuts import render
from cars.models import car
from brands.models import car_brand

def home (request,brand_slug = None) :
    data = car.objects.all()
    brands = car_brand.objects.all()
    if brand_slug is not None:
        brand = car_brand.objects.get(slug = brand_slug)
        data = car.objects.filter(brand_name = brand)

    return render (request, 'home.html', {"data":data, "brands":brands})