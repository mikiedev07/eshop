from .models import Cart, Category, Comment, Product, Picture
from rest_framework import serializers
from .services import Cost


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"

    def create(self, validated_data):
        cart = Cart.objects.create(creator=validated_data["creator"])
        cost = Cost()
        for product in validated_data["products"]:
            cart.products.add(product)
            cost.add_price(product.price - product.price / 100 * product.discount)
        cart.final_cost = round(cost.price, 2)
        cart.save()
        return cart

    def update(self, instance, validated_data):
        instance.creator = validated_data["creator"]
        instance.products.clear()
        cost = Cost()

        for product in validated_data["products"]:
            instance.products.add(product)
            cost.add_price(product.price - product.price / 100 * product.discount)
        instance.final_cost = round(cost.price, 2)
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = "__all__"
