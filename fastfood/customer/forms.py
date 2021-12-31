from django import forms
from django.contrib.auth.forms import UserCreationForm

from main.models import Customer
from phonenumber_field.modelfields import PhoneNumberField


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = PhoneNumberField()

    class Meta:
        model = Customer
        fields = ["username", "password1", "password2", "email", "phone_number"]
