from django.db import models
from categories.models import Categories
from users.models import Users
from comments.models import Comments




class Product(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(max_length=3000)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=False)
    contacts = models.TextField(max_length=500)

    prod_image = models.ManyToManyField(to='Image', blank=True, related_name='prod_image')
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, related_name='products')
    created_by = models.ForeignKey(to=Users, on_delete=models.CASCADE, related_name='created_by')
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name='product_comments_here', blank=True)

    class Meta:
        ordering = ['-time_create']

    def __str__(self):
        return f"{self.title} - {self.description}"


class Image(models.Model):
    image = models.ImageField(upload_to='prod_image/', blank=True, null=True)
    description = models.TextField(blank=True)
