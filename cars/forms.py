from django import forms
from . import models

class AddCarForm (forms.ModelForm):
    class Meta:
        model = models.car
        fields = "__all__"

    def __str__(self):
        return self.name
    

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['name', 'email', 'body']