# -*- coding:utf-8 -*-

from django.http import HttpResponseRedirect


# 如果未登录则跳转到登录界面
def login(func):
    def login_func(request, *args, **kwargs):
        if 'user_id' in request.session.keys():
            return func(request, *args, **kwargs)
        else:
            red = HttpResponseRedirect('/user/login')
            red.set_cookie('url', request.get_full_path())
            return red
    return login_func
