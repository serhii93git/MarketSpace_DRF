from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Categories(MPTTModel):
    cat_name = models.CharField(max_length=50, unique=True)
    cat_description = models.TextField(max_length=500, blank=True, null=True)
    cat_image = models.ImageField(upload_to='cat_image/', blank=True, null=True)
    parent = models.ForeignKey(to='self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    class MTTPMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.cat_name