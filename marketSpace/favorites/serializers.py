from rest_framework import serializers
from .models import SelectedProduct


class SelectedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectedProduct
        fields = '__all__'
