from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

class myUserForm(UserCreationForm):
    image = models.ImageField(name="image")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = " "

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2", "image")

class myLoginForm(AuthenticationForm):
    error_messages = {
        "invalid_login": "Usename, または Password が違います",
        "inactive": "Username が登録されていません",
    }
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.label_suffix = " "

    class Meta:
        model = CustomUser