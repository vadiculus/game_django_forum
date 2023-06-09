from django.shortcuts import render
from .models import Post, Comment
from rest_framework import generics
from django.core.paginator import Paginator
from .serializers import MainPageSerializer, PostsSerializer, CommentsSerializer, PostPageSerializer
from django.db.models import Count, F, Prefetch
from rest_framework.views import APIView
from rest_framework.response import Response
from taggit.models import Tag

class MainPageListView(APIView):
    def get(self, request):
        page_data = {}
        page_data['posts'] = Post.objects.prefetch_related('comments').select_related('author').annotate(
            comments_count=Count('comments'))
        page_data['popular_tags'] = Tag.objects.annotate(posts_count=Count('taggit_taggeditem_items')).order_by('taggit_taggeditem_items')[:10]
        serializer = MainPageSerializer(page_data).data
        return Response(serializer)

class PostDetailsView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk:
            post = Post.objects.prefetch_related(Prefetch('comments', queryset=Comment.objects
                .filter(post=pk)
                .select_related('author')
                .prefetch_related('replies')))\
                .select_related('author').get(pk=pk)
            serializer = PostPageSerializer(post).data
            return Response(serializer)
        else:
            return Response({'error': 'method PUT is not allowed'})

    def post(self, request, *args, **kwargs):
        pass