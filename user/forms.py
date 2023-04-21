from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class UserSignUp(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'birthdate', 'gender', 'password1', 'password2']
        widgets = {
            'birthdate': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)'}
            )
        }