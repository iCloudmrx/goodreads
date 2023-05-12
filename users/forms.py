from django import forms
from django.contrib.auth.models import User
from django.core import validators


class SignUpCreationForm(forms.Form):
    username = forms.CharField(max_length=128,
                               required=True)
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True,
                             validators=[
                                 validators.EmailValidator(
                                     message=("Email yaroqli emas"))
                             ],
                             empty_value="Bo'sh malumot")
    password = forms.CharField(max_length=128,
                               required=True,)

    def validate_email(email):
        print(email)
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email allaqachon ro'yxatdan o'tilgan")
        return email

    def validate_username(username):
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "Username allaqachon ro'yxatdan o'tilgan")
        return username


class LoginForm(forms.Form):
    username = forms.CharField(max_length=128,
                               required=True,
                               widget=forms.TextInput(
                                   attrs={
                                       'autofocus': True
                                   }))
    password = forms.CharField(max_length=128,
                               required=True,
                               widget=forms.PasswordInput(
                                   attrs={
                                       'autocomplete': 'current-password'
                                   }))
