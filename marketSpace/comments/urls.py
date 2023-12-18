from django.urls import path


from .views import CommentAddView, CommentUpdateView


urlpatterns = [
    path('comment/', CommentAddView.as_view(), name='create-comment'),
    path('comment/<int:pk>', CommentUpdateView.as_view(), name='update-comment'),
]
