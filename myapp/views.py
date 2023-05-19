from django.shortcuts import redirect, render
from django.contrib.auth.password_validation import validate_password # 以下追記箇所(6～7行目)
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .forms import myUserForm


def index(request):
    return render(request, "myapp/index.html")

def signup_view(request):
    error_message = ""
    form = myUserForm()
    return render(request, "myapp/signup.html", {'form': form})

def login_view(request):
    return render(request, "myapp/login.html")

def friends(request):
    return render(request, "myapp/friends.html")

def talk_room(request):
    return render(request, "myapp/talk_room.html")

def setting(request):
    return render(request, "myapp/setting.html")

def Registration(request):
    if request.POST:
        form = myUserForm(request.POST, request.FILES)

        if form.is_valid():
            print("************VALID*********************")
            data = form.cleaned_data
            form.save()
            return render(request, "myapp/ok.html")

        else:
            print("************INVALID*********************")
            return render(request, "myapp/signup.html", {'form': form})

    else:
        print("******************NOT POST *****************")
    return render(request, "myapp/index.html")
