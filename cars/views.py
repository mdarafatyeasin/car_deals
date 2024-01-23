from django.shortcuts import render,redirect
from .forms import AddCarForm
from django.contrib import messages
from django.views.generic import DetailView
from . import models

# Create your views here.
def add_Car(request):
    if request.method == "POST":
        add_car_form = AddCarForm(request.POST, request.FILES)
        if add_car_form.is_valid():
            messages.success(request, "Car Added")
            add_car_form.save()
            return redirect("add_car")
    else:
        add_car_form = AddCarForm()
    return render(request, "add_car.html", {"form": add_car_form})


class CarDetails(DetailView):
    model = models.car
    pk_url_kwarg = "id"
    template_name = "car_detail.html"
    def get(self, request, *args, **kwargs):
        # Access and print the current user's ID
        user_id = request.user.id
        print(request.user.id)
        return super().get(request, *args, **kwargs)