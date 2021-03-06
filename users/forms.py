from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Members
from django.forms import ModelForm, fields

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SubscriptionForm(ModelForm):
    class Meta:
        model = Members
        fields = ['location']