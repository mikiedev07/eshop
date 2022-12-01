from .models import Cart, Category, Comment, Product, Picture
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# class CartSerializer(serializers.Serializer):
#     # creator = serializers.ForeignKey(User, on_delete=models.CASCADE)
#     # products = models.ManyToManyField(Product)
#     # final_cost = models.FloatField(blank=True, null=True)
#     def create(self, validated_data):
#         return Cart.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         print("\n\ninstance: ", instance)
#         print("\n\nv_data: ", validated_data)

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = '__all__'
