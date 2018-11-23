from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("", index),
    re_path(r'list_(\d+)_(\d+)_(\d+)/$', list),
    re_path(r'detail_(\d+)/$', detail),
]
