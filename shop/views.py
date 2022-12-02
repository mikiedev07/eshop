from rest_framework.viewsets import ModelViewSet
from django.shortcuts import redirect

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


def clear_cart(request, pk):
    cart = Cart.objects.get(id=pk)
    cart.products.clear()
    cart.final_cost = 0
    cart.save()
    return redirect("swagger-ui")
