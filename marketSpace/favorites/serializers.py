from rest_framework import serializers
from .models import SelectedProduct


class SelectedProductSerializer(serializers.ModelSerializer):

    def perform_create(self, serializer):
        serializer.save(users=[self.request.user])

    class Meta:
        model = SelectedProduct
        fields = '__all__'
