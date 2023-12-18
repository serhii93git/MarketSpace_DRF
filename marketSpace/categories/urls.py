from django.urls import path


from .views import CategoriesView


urlpatterns = [
    path('cat/', CategoriesView.as_view(), name='cat-list'),
]
