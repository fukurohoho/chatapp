from django.contrib import admin

from .models import CustomUser, Talk_content

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Talk_content)
