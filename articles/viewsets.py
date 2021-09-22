from rest_framework import viewsets
from . import models
from . import serializers

class ArticlesViewset(viewsets.ModelViewSet):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticlesSerializer