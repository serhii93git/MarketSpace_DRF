from rest_framework import generics, permissions
from .models import Product, Image
from .serializers import ProductSerializer, ImageSerializer


# class ProductAddView(generics.CreateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


class ProductsListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        sort_by = self.request.query_params.get('sort_by', '-time_create')
        return Product.objects.all().order_by(sort_by)

    """/prod/?sort_by=-time_create для сортування за датою 
    створення у низхідному порядку 
    або /prod/?sort_by=price для сортування 
    за ціною у зростаючому порядку"""


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ImageAddView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Image.objects.filter(created_by=self.request.user)

    serializer_class = ImageSerializer
