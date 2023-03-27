from django.db import models
from accounts.models import User
from taggit.managers import TaggableManager
from mptt import models as mptt_models

class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Контент")
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Автор")
    tags = TaggableManager()
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Comment(mptt_models.MPTTModel):
    content = models.TextField(verbose_name="Контент")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name="Пост")
    parent = mptt_models.TreeForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies',
                                verbose_name="Комментарий")
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Автор")
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created']
