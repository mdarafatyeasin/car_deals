from django.urls import path
from .views import add_Car

urlpatterns = [
    path("add_car", add_Car, name="add_car")
]