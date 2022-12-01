from django.contrib import admin
from .models import Picture, Product, Comment, Category, Cart

#
# class PictureInline(admin.ModelAdmin):
#     exclude = ("final_cost",)
#     readonly_fields = ("final_cost",)


admin.site.register(Picture)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Cart)

