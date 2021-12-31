'''from django import forms
from main.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        fields = ['user_name', 'password1','password2', 'first_name', 'last_name', 'salary']
        widgets = {'user_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'password1': forms.TextInput(attrs={'class': 'form-control'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'salary': forms.NumberInput(attrs={'class': 'form-control'}),
                   }
'''

from django import forms
from django.contrib.auth.forms import UserCreationForm

from main.models import Employee


class EmployeeForm(UserCreationForm):

    class Meta:
        model = Employee
        fields = ['user_name', 'password1', 'password2',
                  'first_name', 'last_name', 'salary']
