from rest_framework import serializers
from .models import Base, Size, Option, Product, Property, Material


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = '__all__'


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    base = BaseSerializer()
    sizes = SizeSerializer()
    materials = MaterialSerializer()
    options = OptionSerializer()

    class Meta:
        model = Property
        fields = ('base', 'sizes', 'materials', 'options')


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'image', 'title', 'price', 'slug')


class ProductDetailSerializer(serializers.ModelSerializer):
    properties = PropertySerializer()

    class Meta:
        model = Product
        fields = '__all__'
