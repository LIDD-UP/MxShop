# -*- coding: utf-8 -*-

#通过django实现json返回

from django.views.generic.base import View
# from django.views.generic import ListView

from goods.models import Goods

class GoodsListView(View):
    def get(self,requests):
        # 实现商品列表展示
        json_list = []
        goods = Goods.objects.all()[:10]

        #通过一个个填写字段；
        # for good in goods:
        #     json_dict = {}
        #     json_dict["name"] = good.name
        #     json_dict["category"] = good.category.name
        #     json_dict["market_price"] = good.market_price
        #     json_list.append(json_dict)

        #通过model_to_dict实现json转化成dict
        # from django.forms.models import model_to_dict #将数据转化为dict的形式
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)

        import json
        from django.core  import serializers
        json_data = serializers.serialize("json",goods)
        json_data = json.loads(json_data) #将str文件转化成dict文件
        from django.http import HttpResponse,JsonResponse
        import json
        return JsonResponse(json_data,safe=False)


