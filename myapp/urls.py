from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup_view, name='signup_view'),
    path('login', views.login_view, name='login_view'),
    path('friends/<int:id>', views.friends, name='friends'),
    path('talk_room/<int:id1>/<int:id2>', views.talk_room, name='talk_room'),
    path('setting/<int:id>/<int:what>', views.setting, name='setting'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)