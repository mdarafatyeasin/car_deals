from django.shortcuts import render,redirect
from .forms import AddCarForm
from django.contrib import messages

# Create your views here.
def add_Car(request):
    if request.method == "POST":
        add_car_form = AddCarForm(request.POST)
        if add_car_form.is_valid():
            messages.success(request, "Car Added")
            add_car_form.save()
            return redirect("add_car")
    else:
        add_car_form = AddCarForm()
    return render(request, "add_car.html", {"form": add_car_form})