from django.urls import path
from rest_framework import routers
from django.urls import include

from .views import (
    CategoryViewSet,
    PictureViewSet,
    ProductViewSet,
    CommentViewSet,
    CartViewSet,
    clear_cart,
)

router = routers.DefaultRouter()
router.register("categories", CategoryViewSet, basename="categories")
router.register("pictures", PictureViewSet, basename="pictures")
router.register("products", ProductViewSet, basename="products")
router.register("comments", CommentViewSet, basename="comments")
router.register("carts", CartViewSet, basename="carts")

app_name = "shop"
urlpatterns = [path("purchase/<int:pk>/", clear_cart)]

urlpatterns += router.urls
