from django.contrib import admin
from django.urls import path
from Login_out import views

urlpatterns = [
    path("signup/", views.Signup, name="Signup"),
    path("Home/", views.Home , name='Home'),
    path("Login/", views.Login, name="Login")
]
