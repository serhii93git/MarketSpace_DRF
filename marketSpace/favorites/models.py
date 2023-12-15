from django.db import models
from django.contrib.auth import get_user_model  # get AUTH_USER_MODEL from settings.py
from products.models import Product

User = get_user_model()


class SelectedProduct(models.Model):
    users = models.ManyToManyField(User, related_name='selected_products')
    products = models.ManyToManyField(Product, related_name='selected_by_users')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{', '.join(user.username for user in self.users.all())} - {', '.join(product.title for product in self.products.all())}"
