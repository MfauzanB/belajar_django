from django.contrib.auth.models import Permission
from articles.models import Article
from articles.serializers import article_serializer
from rest_framework import viewsets, permissions

class kelompokviewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = article_serializer
