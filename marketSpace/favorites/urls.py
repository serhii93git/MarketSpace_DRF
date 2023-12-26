from django.urls import path


from .views import SelectedProductAddView, SelectedProductListView, SelectedProductDeleteView

urlpatterns = [
    path('fav/', SelectedProductAddView.as_view(), name='add-favorite'),
    path('fav-list/', SelectedProductListView.as_view(), name='list-favorite'),
    path('fav/<int:pk>', SelectedProductDeleteView.as_view(), name='delete-favorite'),
]
