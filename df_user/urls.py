from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register),
    path('register_handle/', register_handle),
    path('register_exist/', register_exist),
    path('login/', login),
    path('login_handle/', login_handle),
    path('info/', info),
    path('order/', order),
    path('site/', site),
]
