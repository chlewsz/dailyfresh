from django.shortcuts import render, redirect
from df_user import user_decorator
from django.http import JsonResponse, HttpResponse
from .models import *


@user_decorator.login
def cart(request):
    uid = request.session['user_id']
    carts = CartInfo.objects.filter(user_id=uid)
    context = {'title': '购物车',
               'page_name': 1,
               'carts': carts}
    return render(request, 'df_cart/cart.html', context)


@user_decorator.login
def add(request, goods_id, count):
    uid = request.session['user_id']
    goods_id = int(goods_id)
    count = int(count)

    carts = CartInfo.objects.filter(user_id=uid, goods_id=goods_id)

    if len(carts) >= 1:
        cart = carts[0]
        cart.count = cart.count + count
    else:
        cart = CartInfo()
        cart.user_id = uid
        cart.goods_id = goods_id
        cart.count = count

    cart.save()

    if request.is_ajax():
        count = CartInfo.objects.filter(user_id=uid).count()
        return JsonResponse({'count': count})
    else:
        return redirect('/cart/')


@user_decorator.login
def edit(request, cart_id, count):
    try:
        cart_id = int(cart_id)
        cart = CartInfo.objects.get(pk=cart_id)
        count = int(count)
        count1 = cart.count = count
        cart.save()

        data = {'ok': 0}
    except:
        data = {'ok': count1}
    return JsonResponse(data)


@user_decorator.login
def delete(request, cart_id):
    try:
        cart_id = int(cart_id)
        cart = CartInfo.objects.get(pk=cart_id)
        cart.delete()

        data = {'ok': 1}
    except:
        data = {'ok': 0}
    return JsonResponse(data)
