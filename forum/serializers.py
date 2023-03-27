from rest_framework import serializers
from forum.models import Post, Comment
from taggit.models import Tag
from accounts.serializers import UserSerializer


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, instance):
        print(self.parent.parent.__class__)
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


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
    author = UserSerializer(read_only=True)
    replies = RecursiveSerializer(read_only=True, many=True)

    class Meta:
        model = Comment
        fields = ('id','parent','content','author', 'replies', 'created')

class MainPageSerializer(serializers.Serializer):
    posts = PostsSerializer(read_only=True, many=True)
    popular_tags = TagsSerializer(read_only=True, many=True)

class PostPageSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentsSerializer(read_only=True, many=True)
    class Meta:
        model = Post
        fields = '__all__'