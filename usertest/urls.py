from django.urls import path
from usertest import views

urlpatterns = [
    path('users', views.userlist, name = 'users'),
]