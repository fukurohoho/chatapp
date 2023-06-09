from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # user_name = forms.Charfield()
    # email = forms.EmailField()
    # password = forms.Charfield(widget=forms.PasswordInput,validators=[MinLengthValidator(6)])
    image = models.ImageField(upload_to=None, height_field=None, width_field=None)

