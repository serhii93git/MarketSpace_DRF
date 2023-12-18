from rest_framework import generics
from .models import Categories
from .serializers import CategorySerializer


class CategoriesView(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
