from django.db import models
from users.models import Users



class Comments(models.Model):
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='replies')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(to='products.Product', on_delete=models.CASCADE, related_name='comments_here', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} : {self.text[:50]}'

