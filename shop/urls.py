from django.urls import path

from .views import (
    CategoryAPIView,
    PictureAPIView,
    SupplierAPIView,
    ProductAPIView,
    CommentAPIView,
    CartAPIView,
)

app_name = 'shop'
urlpatterns = [
    path('categories/', CategoryAPIView.as_view()),
    path('pictures/', PictureAPIView.as_view()),
    path('suppliers/', SupplierAPIView.as_view()),
    path('products/', ProductAPIView.as_view()),
    path('comments/', CommentAPIView.as_view()),
    path('carts/', CartAPIView.as_view()),
]
