from rest_framework import serializers, status
from rest_framework import response
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import mixins

from .serializers import PostSerializer
from api.models import Post

class TestView(APIView):

    permission_classes = [IsAuthenticated, ]

    def get(self, request, *arg, **kwargs):
        qs = Post.objects.all()
        post = qs.first()
        # serializer = PostSerializer(qs, many=True)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class PostView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    def get(self, request, *arg, **kwargs):
        return self.list(request, *arg, **kwargs)

    def post(self, request, *arg, **kwargs):
        return self.create(request, *arg, **kwargs)

class PostCreateView(
    mixins.ListModelMixin,
    generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *arg, **kwargs):
        return self.list(request, *arg, **kwargs)

class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

  

