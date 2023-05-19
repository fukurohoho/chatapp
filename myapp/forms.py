from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django import forms


class myUserForm(UserCreationForm):
    image = models.ImageField(name="image")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = " "

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2", "image")

        error_messages = {
            "password1": {
                "requied": "入力してください"
            }
        }