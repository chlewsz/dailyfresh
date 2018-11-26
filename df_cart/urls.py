from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', cart),
    re_path(r'add_(\d+)_(\d+)/', add),
    re_path(r'del_(\d+)/', delete),
    re_path(r'edit_(\d+)_(\d+)/', edit),
]
