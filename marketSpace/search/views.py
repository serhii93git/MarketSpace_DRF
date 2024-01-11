from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer


class SearchView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        query = self.request.query_params.get('search_query', '')
        return Product.objects.filter(title__icontains=query)
    # /search/?search_query='назва_товару' для здійснення пошуку товарів за назвою через API.
