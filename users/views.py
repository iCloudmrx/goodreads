from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from .forms import SignUpCreationForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

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
            password = request.POST['password']
            user = User.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            user.set_password(password)
            user.save()
            return redirect('users:login')
        else:
            return render(request, 'users/register.html', {
                'form': SignUpCreationForm()
            })


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
