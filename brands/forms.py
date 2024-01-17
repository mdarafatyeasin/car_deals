from django import forms
from .models import car_brand

class addModel(forms.ModelForm):
    class Meta:
        model = car_brand
        fields = "__all__"