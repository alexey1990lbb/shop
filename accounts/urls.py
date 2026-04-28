from django.urls import path
from .views import login_view, register, profile_view, logout_view

app_name = 'core'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile_view, name='profile'),
]