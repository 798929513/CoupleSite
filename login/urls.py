from django.urls import path
from login import views

app_name = "login"

urlpatterns = [
    path('', views.login_and_register, name="loginAndRegister"),
    path('loginAndRegister/', views.login_and_register, name="loginAndRegister"),
    path('index/', views.index, name="index"),
    path('logout/', views.logout, name="logout"),
]

