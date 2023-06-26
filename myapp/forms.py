from .models import CustomUser, Talk_content, Content
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

class ChatInputForm(forms.ModelForm):
    class Meta:
        model = Talk_content
        # exclude = ["user_from", "user_to"]
        fields = ("user_from","user_to","chat_content",)

    """
    def __init__(self, user_from=None, user_to=None, chat_content=None, *args, **kwargs,):
        print(f"user_from: {user_from}    user_to:  {user_to}  content: {chat_content}")
        self.user_from = user_from
        self.user_to = user_to
        self.chat_content = chat_content
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if self.chat_content == "":
            return
        obj = super().save(commit=False)
        if self.user_from:
            obj.user_from = self.user_from
        if self.user_to:
            obj.user_to = self.user_to
        if self.chat_content:
            obj.chat_content = self.chat_content
        if commit:
            obj.save()
        return obj
    """