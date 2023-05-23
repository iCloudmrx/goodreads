from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .forms import SignUpCreationForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django_email_verification import send_email
from django.contrib.auth.models import User
# Create your views here.


class RegisterView(View):
    def get(self, request):
        form = SignUpCreationForm()
        return render(request, 'users/register.html', {
            'form': form
        })

    def post(self, request):
        form = SignUpCreationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password1']
            user = User.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            user.set_password(password)
            user.is_active = False
            user.is_staff = False
            # send_email(user)
            user.save()
            return redirect('home')
        else:
            return render(request, 'users/register.html', {
                'form': SignUpCreationForm()
            })


def confirm_needed(request, id):
    user = User.objects.get(id=id)
    if user.is_active == True:
        redirect('users:login')
    else:
        return render(request, 'confirm_needed.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html', {
            'form': LoginForm()
        })

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'users/login.html', {
                    'form': LoginForm(data=request.POST)
                })
        else:
            return render(request, 'users/login.html', {
                'form': LoginForm()
            })


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/profile.html', {
            'user': request.user
        })


class LogOutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('home')
