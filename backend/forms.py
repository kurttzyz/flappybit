from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class RegisterationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'mobile_number')