from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators


class SignUpCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']

    def validate_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email allaqachon ro'yxatdan o'tilgan")
        return email

    def validate_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "Username allaqachon ro'yxatdan o'tilgan")
        return username

    def validate_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("Password bir xil emas")
        return password2


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
