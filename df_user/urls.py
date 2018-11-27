from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('register/', register),
    path('register_handle/', register_handle),
    path('register_exist/', register_exist),
    path('login/', login),
    path('logout/', logout),
    path('login_handle/', login_handle),
    path('info/', info),
    re_path('order(\d*)/', order),
    path('site/', site),
    path('site2/', site2),
]
