from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/forum/', include('forum.urls', namespace='forum')),
]
