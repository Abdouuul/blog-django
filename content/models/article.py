from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='articles', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False, verbose_name='Publié')
    publication_date = models.DateTimeField(null=True, blank=True, verbose_name='Date de publication')
    image = models.ImageField(upload_to='articles/', null=True, blank=True, verbose_name='Image')
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'