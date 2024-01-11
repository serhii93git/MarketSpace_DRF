from django.urls import path


from .views import ProductDetailView, ProductsListView, ImageAddView
urlpatterns = [
    path('prod/', ProductsListView.as_view(), name='prod-list'),
    # path('prod-add/', ProductAddView.as_view(), name='prod-add'),
    path('prod/<int:pk>', ProductDetailView.as_view(), name='prod-detail'),
    path('img/', ImageAddView.as_view(), name='many-img-add-for-prod')
]
