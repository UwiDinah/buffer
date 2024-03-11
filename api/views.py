from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PosttView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)