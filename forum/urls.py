from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.MainPageListView.as_view(), name='index'),
    path('posts/<int:pk>', views.PostDetailsView.as_view(), name='post_details')
]
