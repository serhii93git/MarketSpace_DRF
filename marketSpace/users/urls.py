from django.urls import path


from .views import UserAddView, UserUpdateView
urlpatterns = [
    path('user/', UserAddView.as_view(), name='user-add'),
    path('user/<int:pk>', UserUpdateView.as_view(), name='User-update'),

]
