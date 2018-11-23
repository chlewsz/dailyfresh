from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, Page


def index(request):
    type_list = TypeInfo.objects.all()
    type0 = type_list[0].goodsinfo_set.order_by("-id")[0:4]
    type01 = type_list[0].goodsinfo_set.order_by("-gclick")[0:4]
    type1 = type_list[1].goodsinfo_set.order_by("-id")[0:4]
    type11 = type_list[1].goodsinfo_set.order_by("-gclick")[0:4]
    type2 = type_list[2].goodsinfo_set.order_by("-id")[0:4]
    type21 = type_list[2].goodsinfo_set.order_by("-gclick")[0:4]
    type3 = type_list[3].goodsinfo_set.order_by("-id")[0:4]
    type31 = type_list[3].goodsinfo_set.order_by("-gclick")[0:4]
    type4 = type_list[4].goodsinfo_set.order_by("-id")[0:4]
    type41 = type_list[4].goodsinfo_set.order_by("-gclick")[0:4]
    type5 = type_list[5].goodsinfo_set.order_by("-id")[0:4]
    type51 = type_list[5].goodsinfo_set.order_by("-gclick")[0:4]

    context = {'title': '首页', 'guest_cart': 1,
               'type0': type0, 'type01': type01,
               'type1': type1, 'type11': type11,
               'type2': type2, 'type21': type21,
               'type3': type3, 'type31': type31,
               'type4': type4, 'type41': type41,
               'type5': type5, 'type51': type51}
    return render(request, 'df_goods/index.html', context)


def list(request, type_id, pindex, sort):
    typeinfo = TypeInfo.objects.get(pk=int(type_id))
    news = typeinfo.goodsinfo_set.order_by('-id')[0:2]

    goods_list = GoodsInfo.objects.filter(gtype_id=int(type_id))

    if sort == '1':  # 默认
        goods_list = goods_list.order_by('-id')
    elif sort == '2':  # 价格
        goods_list = goods_list.order_by('-gprice')
    elif sort == '3':  # 人气/点击量
        goods_list = goods_list.order_by('-gclick')

    paginator = Paginator(goods_list, 10)
    page = paginator.get_page(int(pindex))

    context = {'title': '列表', 'guest_cart': 1,
               'page': page, 'paginator': paginator,
               'typeinfo': typeinfo, 'sort': sort,
               'news': news}
    return render(request, 'df_goods/list.html', context)


def detail(request, goods_id):
    goods = GoodsInfo.objects.get(pk=int(goods_id))
    goods.gclick = goods.gclick + 1
    goods.save()

    news = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context = {'title': '详情', 'guest_cart': 1, 'id': goods_id, 'goods': goods, 'news': news, 'typeinfo': goods.gtype}
    return render(request, 'df_goods/detail.html', context)
