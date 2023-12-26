from rest_framework import generics, permissions
from .models import Product, Image
from .serializers import ProductSerializer, ImageSerializer


class ProductAddView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductsListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ImageAddView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Image.objects.filter(created_by=self.request.user)

    serializer_class = ImageSerializer
