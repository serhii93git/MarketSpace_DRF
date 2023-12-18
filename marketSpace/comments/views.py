from rest_framework import generics
from .models import Comments
from .serializers import CommentSerializer


class CommentAddView(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer


class CommentUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
