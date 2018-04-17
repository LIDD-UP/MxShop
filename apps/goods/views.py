#coding:utf8

from .serializers import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response#比原来的django的response强大
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import Goods

#通过genericview实现商品的展示；
#继承了两个model
class GoodsListView(generics.ListAPIView):
    queryset = Goods.objects.all()[:10]
    serializer_class = GoodsSerializer


#自己定制分页：
class










# # 通过apiview实现serializer
# class GoodsListView(APIView):
#     """
#     List all Goods, or create a new goods.
#     """
#     def get(self, request, format=None):
#         goods = Goods.objects.all()[:10]
#         goods_serializer = GoodsSerializer(goods, many=True)
#         #通过新的序列化来序列化goods(many是将goods序列化成一个数组）
#         return Response(goods_serializer.data)
#
#     # 接受前端传送过来的数据
#     def post(self,request,format=None):
#         serializer = GoodsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
