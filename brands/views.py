from django.shortcuts import render,redirect
from .forms import addCarBrand
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_brand(request):
    if request.method == "POST":
        add_brand_form = addCarBrand(request.POST)
        if add_brand_form.is_valid():
            messages.success(request, "Car brand added successfully")
            add_brand_form.save()
            return redirect("add_brand")
    else:
        add_brand_form = addCarBrand()
    return render (request, 'add_brand.html', {"form":add_brand_form})