from django.shortcuts import redirect, render
from django.contrib.auth.password_validation import validate_password # 以下追記箇所(6～7行目)
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .forms import myUserForm, myLoginForm
from django.contrib.auth.views import LoginView

from PIL import Image

def trimming_square(imgpath):
    img = Image.open(imgpath)
    new_size = min(img.width, img.height)
    center_x = int(img.width / 2)
    center_y = int(img.height / 2)

    img_crop = img.crop((center_x - new_size / 2, center_y - new_size / 2, center_x + new_size / 2, center_y + new_size / 2))
    img_crop.save(imgpath)

    print("******** Trimming Completed. *************")



def index(request):
    return render(request, "myapp/index.html")

def signup_view(request):
    if request.POST:
        form = myUserForm(request.POST, request.FILES)

        if form.is_valid():
            print("************VALID*********************")
            new_username = request.POST["username"]

            data = form.cleaned_data
            # CustomUser.objects.get(username="user04").delete()

            form.save()
            new_user = CustomUser.objects.get(username=new_username)
            picpath = new_user.image.url
            trimming_square("./"+picpath[1:]) # 正方形じゃない画像はトリミングする

            return render(request, "myapp/ok.html")

        else:
            print("************INVALID*********************")
            return render(request, "myapp/signup.html", {'form': form})

    else:
        print("******************NOT POST*****************")
        form = myUserForm()
        return render(request, "myapp/signup.html", {'form': form})

def login_view(request):
    if request.POST:
        form = myLoginForm(request, data=request.POST)

        if form.is_valid():
            print("************Login Sccess*********************")
            return friends(request)

        else:
            print("************Login Failed*********************")
            return render(request, "myapp/login.html", {'form': form})
    
    else:
        print("******************NOT POST *****************")
        form = myLoginForm()
        return render(request, "myapp/login.html", {'form': form})

def friends(request):    
    myusername = request.POST["username"]
    user_all = CustomUser.objects.all()
    
    user_li = [{"username": user.username, "image": user.image.url} for user in user_all if user.username != myusername]

    return render(request, "myapp/friends.html", {"username": myusername, "friends": user_li})

def talk_room(request):
    return render(request, "myapp/talk_room.html")

def setting(request):
    return render(request, "myapp/setting.html")