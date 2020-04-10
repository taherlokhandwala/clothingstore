from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Address


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


class EditUser(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class NewAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = "__all__"
        exclude = ("customer_user_name",)
