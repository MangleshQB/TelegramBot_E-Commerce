from rest_framework import serializers

from products.models import Product
from category.models import Category
from category.serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'slug',
            'price',
            'description',
            'offer_badge',
            'popular_items',
            'new_arrivals',
            'instock',
            'width_field',
            'height_field',
            'image',
            'category',
        )

    def get_category(self, obj):
        response = CategorySerializer(obj.category).data
        return response
