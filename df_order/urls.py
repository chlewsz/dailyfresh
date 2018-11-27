from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', order),
    path('handle/', order_handle),
]
