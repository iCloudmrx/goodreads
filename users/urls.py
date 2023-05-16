from django.urls import path
from .views import RegisterView, LoginView, ProfileView, LogOutView,confirm_needed

app_name = 'users'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm-needed/<int:id>/',confirm_needed,name='confirm_needed'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile')
]
