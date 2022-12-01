from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from django.http import Http404
from .services import Cost

from .models import (
    Category,
    Cart,
    Picture,
    Comment,
    Product,
)
from .serializers import (
    CategorySerializer,
    CartSerializer,
    PictureSerializer,
    CommentSerializer,
    ProductSerializer,
)


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class PictureViewSet(ModelViewSet):
    serializer_class = PictureSerializer
    queryset = Picture.objects.all()


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CartViewSet(ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()


# class CartListView(APIView):
#     def get(self, request, format=None):
#         carts = Cart.objects.all()
#         serializer = CartSerializer(carts, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         request.data['final_cost'] = 0
#         serializer = CartSerializer(data=request.data)
#         cost = Cost()
#
#         if serializer.is_valid():
#             for i in request.data['products']:
#                 p = Product.objects.get(id=i)
#                 cost.add_price(p.price - p.price / 100 * p.discount)
#             serializer.validated_data['final_cost'] = round(cost.price, 2)
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class CartDetailView(APIView):
#     def get_object(self, pk):
#         try:
#             return Cart.objects.get(pk=pk)
#         except Cart.DoesNotExist:
#             raise Http404
#
#     def put(self, request, id, format=None):
#         cart = self.get_object(id)
#         serializer = CartSerializer(cart, data=request.data)
#         prices = []
#         for i in cart.products.all():
#             p = Product.objects.get(title=i)
#             prices.append(p.price)
#
#         if serializer.is_valid():
#             for i in request.data['products']:
#                 if i not in prices:
#                     p = Product.objects.get(id=i)
#                     serializer.validated_data['final_cost'] += p.price - p.price / 100 * p.discount
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, id, format=None):
#         cart = self.get_object(id)
#         cart.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
