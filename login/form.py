from django import forms
from .models import User


class RegisterForm(forms.Form):
    username_register = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(
        attrs={
            'placeholder' : '用户名'
        }
    ))
    email = forms.EmailField(label="邮箱", widget=forms.EmailInput(
        attrs={
            'placeholder': '邮箱'
        }
    ))
    password_register = forms.CharField(label="密码", max_length=128, widget=forms.PasswordInput(
        attrs={
            'placeholder': '密码'
        }
    ))
    confirm_pass = forms.CharField(label="确认密码", max_length=128, widget=forms.PasswordInput(
        attrs={
            'placeholder': '确认密码'
        }
    ))


class LoginForm(forms.Form):
    username_login = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(
        attrs={
            'placeholder' : '用户名'
        }
    ))
    password_login = forms.CharField(label="密码", max_length=128, widget=forms.PasswordInput(
        attrs={
            'placeholder': '密码'
        }
    ))


