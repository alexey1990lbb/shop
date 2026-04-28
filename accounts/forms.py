from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(label='Телефон', max_length=20, required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'phone')