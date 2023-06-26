from django.shortcuts import redirect, render
from django.contrib.auth.password_validation import validate_password # 以下追記箇所(6～7行目)
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Talk_content
from .forms import myUserForm, myLoginForm, ChatInputForm
from django.contrib.auth.views import LoginView
from django.db.models import Q
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

            form.save()
            new_user = CustomUser.objects.get(username=new_username)
            picpath = new_user.image.url
            trimming_square("./"+picpath[1:]) # 正方形じゃない画像はトリミングする

            return render(request, "myapp/index.html")

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
    myid = CustomUser.objects.get(username=myusername).id
    user_all = CustomUser.objects.all()
    
    user_li = [{"username": user.username, "image": user.image.url, "id": user.id} for user in user_all if user.username != myusername]

    return render(request, "myapp/friends.html", {"id": myid, "username": myusername, "friends": user_li})

def talk_room(request, id1, id2):
    user1 = CustomUser.objects.get(id=id1).username
    user2 = CustomUser.objects.get(id=id2).username

    if request.POST:
        chat_content = request.POST["chat_content"]
        # request.POST["user_from"] = user1
        # request.POST["user_to"] = user2
        print(type(chat_content))
        new_message = ChatInputForm({"user_from": user1, "user_to": user2, "chat_content": chat_content})# | request.POST)
        print(f"POST {request.POST}")
        if new_message.is_valid():
            print("***VALID******")
            new_message.save()
        else:
            print("***INAVLID***")

            #new_message.save()
    # talkroom 表示
    contents = Talk_content.objects.filter(Q(user_to=user1, user_from=user2)|Q(user_to=user2, user_from=user1))

    messages = []
    for content_ in contents:
        if content_.chat_content == "":
            continue
        messages.append({"time": content_.time, "from": content_.user_from, "to": content_.user_to, "message": content_.chat_content})
    messages = sorted(messages, key=lambda x: x['time'])

    for i in range(len(messages)):
        #messages[i]["time"] = messages[i]["time"].strftime("%m/%d %H:%M")
        pass


    form = ChatInputForm()
    #print(f"messages:  {messages}")
    #print(type(messages[0]["time"]))
    data = {
        "myusername": user1,
        "myid": id1,
        "your_id": id2,
        "to_username": user2,
        "messages": messages,
        "form": form
    }
    return render(request, "myapp/talk_room.html", data)

def setting(request):
    return render(request, "myapp/setting.html")