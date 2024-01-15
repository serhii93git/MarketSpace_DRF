from django.urls import path


from .views import ProductDetailView, ProductsListView, ImageAddView, ImageListView, ImageDetailView
urlpatterns = [
    path('prod/', ProductsListView.as_view(), name='prod-list'),
    # path('prod-add/', ProductAddView.as_view(), name='prod-add'),
    path('prod/<int:pk>', ProductDetailView.as_view(), name='prod-detail'),
    # path('img/', ImageAddView.as_view(), name='many-img-add-for-prod'),
    # path('image/', ImageListView.as_view(), name='imahe-list'),
    # path('image/<int:pk>/', ImageDetailView.as_view(), name='image-detail'),

]
