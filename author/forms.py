from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# forms
# registration
class registration_form (UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'id_required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'id_required'}))
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

# edit user data
class edit_user_data(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


