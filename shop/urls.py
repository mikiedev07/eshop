from django.urls import path
from rest_framework import routers
from django.urls import include

from .views import (
    CategoryViewSet,
    PictureViewSet,
    ProductViewSet,
    CommentViewSet,
    CartViewSet,
    # CartListView,
    # CartDetailView,
)

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('pictures', PictureViewSet, basename='pictures')
router.register('products', ProductViewSet, basename='products')
router.register('comments', CommentViewSet, basename='comments')
router.register('carts', CartViewSet, basename='carts')

app_name = 'shop'
urlpatterns = [
    # path('carts/', CartListView.as_view()),
    # path('carts/<int:id>', CartDetailView.as_view()),
]

urlpatterns += router.urls
