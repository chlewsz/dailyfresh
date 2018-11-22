# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect
from .models import *
from hashlib import sha1
from django.http import JsonResponse, HttpResponseRedirect


def register(request):
    context = {"title": "天天生鲜-注册"}
    return render(request, 'df_user/register.html', context)


def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {'title': '天天生鲜-登录', 'error_name': 0, 'error_pwd': 0, 'uname': uname}
    return render(request, 'df_user/login.html', context)


def register_handle(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    ucpwd = post.get('cpwd')
    uemail = post.get('email')

    if upwd != ucpwd:
        return redirect('/user/register/')

    # 密码加密
    s1 = sha1()
    s1.update(bytes(upwd, encoding='utf-8'))
    pwd = s1.hexdigest()

    user = UserInfo()
    user.uname = uname
    user.upwd = pwd
    user.uemail = uemail

    user.save()

    return redirect('/user/login/')


def register_exist(request):
    uname = request.GET.get("uname")
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count': count})


def login_handle(request):
    post = request.POST
    uname = post.get('username')
    pwd = post.get('pwd')
    jizhu = post.get('jizhu', 0)

    users = UserInfo.objects.filter(uname=uname)
    if len(users) == 1:
        s1 = sha1()
        s1.update(bytes(pwd, encoding='utf-8'))
        if s1.hexdigest() == users[0].upwd:
            red = HttpResponseRedirect('/user/info/')
            if jizhu != 0:
                red.set_cookie('uname', uname)
            else:
                red.set_cookie('uname', '', max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red
        else:
            context = {'title': '天天生鲜-登录', 'error_name': 0, 'error_pwd': 1, 'uname': uname, 'upwd': pwd}
            return render(request, 'df_user/login.html', context)
    else:
        context = {'title': '天天生鲜-登录', 'error_name': 1, 'error_pwd': 0, 'uname': uname, 'upwd': pwd}
        return render(request, 'df_user/login.html', context)


def info(request):
    context = {"title": "天天生鲜 - 用户中心"}
    return render(request, 'df_user/user_center_info.html', context)
