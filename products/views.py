from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'slug'
