from rest_framework import serializers
from forum.models import Post, Comment
from taggit.models import Tag


class PostsSerializer(serializers.ModelSerializer):
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)
    class Meta:
        model = Post
        fields = '__all__'

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class MainPageSerializer(serializers.Serializer):
    posts = PostsSerializer(read_only=True, many=True)
    popular_tags = TagsSerializer(read_only=True, many=True)