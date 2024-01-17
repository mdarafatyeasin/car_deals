from django import forms
from . import models

class addCar (forms.ModelForm):
    class Meta:
        model = models.car
        fields = "__all__"

    def __str__(self):
        return self.name