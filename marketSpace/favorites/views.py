from rest_framework import generics, permissions
from .models import SelectedProduct
from .serializers import SelectedProductSerializer


class SelectedProductAddView(generics.CreateAPIView):
    # queryset = SelectedProduct.objects.all()
    serializer_class = SelectedProductSerializer

    def perform_create(self, serializer):
        serializer.save(users=[self.request.user])


class SelectedProductListView(generics.ListAPIView):
    serializer_class = SelectedProductSerializer

    def get_queryset(self):
        return SelectedProduct.objects.filter(users=self.request.user)


class SelectedProductDeleteView(generics.DestroyAPIView):
    serializer_class = SelectedProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SelectedProduct.objects.filter(users=self.request.user)
