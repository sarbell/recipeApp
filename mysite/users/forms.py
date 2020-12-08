from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    firstname = forms.TextInput()
    lastname = forms.TextInput()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class UpdateProfile(forms.ModelForm):
        class Meta:
            model = Profile
            fields = ['image']


