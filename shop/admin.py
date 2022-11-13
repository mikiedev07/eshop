from django.contrib import admin
from .models import Picture, Product, Comment, Category, Supplier, Cart


# class PictureInline(admin.StackedInline):
#     model = Picture
#
#
# class ProductAdmin(admin.ModelAdmin):
#     inlines = [PictureInline]


admin.site.register(Picture)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Cart)

