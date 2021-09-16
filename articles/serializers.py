from django.db.models import fields
from articles.models import Article
from rest_framework import serializers

class article_serializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'slug', 'body', 'date', 'thumb', 'author']