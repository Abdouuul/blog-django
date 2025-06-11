from django.db import models
from .article import Article
from django.contrib.auth.models import User

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='Article')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='comments', verbose_name='Auteur')

    def __str__(self):
        return self.content
    