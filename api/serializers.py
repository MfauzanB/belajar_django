from rest_framework import serializers
from api.models import Post

from django import forms

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'deskripsi', 'timestamp', 'owner')