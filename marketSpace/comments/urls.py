from django.urls import path


from .views import CommentAddView, CommentUpdateView


urlpatterns = [
    path('add-comment/', CommentAddView.as_view()),
    path('add-comment/<int:pk>', CommentUpdateView.as_view()),
]
