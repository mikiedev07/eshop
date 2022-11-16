from django.urls import path

from .views import (
    CategoryListView,
    CategoryDetailAPIView,
    PictureListView,
    PictureDetailView,
    SupplierListView,
    SupplierDetailView,
    ProductListView,
    ProductDetailView,
    CommentListView,
    CommentDetailView,
    CartListView,
    CartDetailView,
)

app_name = 'shop'
urlpatterns = [
    path('categories/', CategoryListView.as_view()),
    path('categories/<int:id>', CategoryDetailAPIView.as_view()),
    path('pictures/', PictureListView.as_view()),
    path('pictures/<int:id>', PictureDetailView.as_view()),
    path('suppliers/', SupplierListView.as_view()),
    path('suppliers/<int:id>', SupplierDetailView.as_view()),
    path('products/', ProductListView.as_view()),
    path('products/<int:id>', ProductDetailView.as_view()),
    path('comments/', CommentListView.as_view()),
    path('comments/<int:id>', CommentDetailView.as_view()),
    path('carts/', CartListView.as_view()),
    path('carts/<int:id>', CartDetailView.as_view()),
]
