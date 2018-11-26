# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect
from .models import *
from hashlib import sha1
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
import json
from . import user_decorator


# 注册
def register(request):
    context = {"title": "注册"}
    return render(request, 'df_user/register.html', context)


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


# 登录
def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {'title': '登录', 'error_name': 0, 'error_pwd': 0, 'uname': uname}
    return render(request, 'df_user/login.html', context)


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
            url = request.COOKIES.get('url', '/')
            red = HttpResponseRedirect(url)
            if jizhu != 0:
                red.set_cookie('uname', uname)
            else:
                red.set_cookie('uname', '', max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red
        else:
            context = {'title': '登录', 'error_name': 0, 'error_pwd': 1, 'uname': uname, 'upwd': pwd}
            return render(request, 'df_user/login.html', context)
    else:
        context = {'title': '登录', 'error_name': 1, 'error_pwd': 0, 'uname': uname, 'upwd': pwd}
        return render(request, 'df_user/login.html', context)


# 个人信息
@user_decorator.login
def info(request):
    user = UserInfo.objects.get(pk=request.session['user_id'])
    context = {"title": "用户中心",
               'user_name': user.uname,
               'user_email': user.uemail,
               'user_address': user.uaddress,
               'page_name': 1}
    return render(request, 'df_user/user_center_info.html', context)


# 全部订单
@user_decorator.login
def order(request):
    context = {'title': '用户中心',
               'page_name': 1}
    return render(request, 'df_user/user_center_order.html', context)


# 收货地址
@user_decorator.login
def site(request):
    user = UserInfo.objects.get(pk=request.session['user_id'])

    # 在form提交时执行该处理
    if request.method == 'POST':
        post = request.POST
        user.ushou = post.get('shou')
        user.uaddress = post.get('site')
        user.uemail = post.get('email')
        user.uphone = post.get('phone')
        user.save()
    context = {'title': '用户中心', 'user': user, 'page_name': 1}
    return render(request, 'df_user/user_center_site.html', context)


@user_decorator.login
def site2(request):
    user = UserInfo.objects.get(pk=request.session['user_id'])

    # 在form提交时执行该处理
    if request.method == 'POST':
        post = request.POST
        user.ushou = post.get('shou')
        user.uaddress = post.get('site')
        user.uemail = post.get('email')
        user.uphone = post.get('phone')
        user.save()
    context = {'title': '用户中心', 'ushou': user.ushou, 'uaddress': user.uaddress, 'uemail': user.uemail, 'uphone': user.uphone}
    print(json.dumps(context))
    return JsonResponse(context)


def logout(request):
    request.session.flush()
    red = HttpResponseRedirect('/')
    red.cookies.clear()
    return red
