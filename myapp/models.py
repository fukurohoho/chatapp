from django.db import models
from django.contrib.auth.forms import UserCreationForm

# Create your models here.
class SignUpClass(UserCreationForm):
    # user_name = forms.Charfield()
    # email = forms.EmailField()
    # password = forms.Charfield(widget=forms.PasswordInput,validators=[MinLengthValidator(6)])
    image = ImageField(upload_to=None, height_field=None, width_field=None)

    
