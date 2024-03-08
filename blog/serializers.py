from rest_framework import serializers
from .models import Post

# Serializer for Post model
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content']
