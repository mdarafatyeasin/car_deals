from django.urls import path
from .views import add_Car,CarDetails,detail_view

urlpatterns = [
    path("add_car", add_Car, name="add_car"),
    # path("car_detail/<int:id>", CarDetails.as_view(), name="car_detail"),
    path("car_detail/<int:id>", detail_view.as_view(), name="car_detail"),
    path("bye_now/<int:id>", CarDetails.as_view(), name="car_bye"),
]