from django.contrib import admin
from django.utils.html import format_html
from .models.article import Article
from .models.comment import Comment

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['author', 'title']
    list_display = ['title', 'created_at', 'author_name', 'content_length', 'is_published', 'thumbnail_image']
    ordering = ['-created_at']
    fieldsets = [
        
        ('Auteur & Publication', {
            'fields': ['author', 'is_published', 'publication_date']
            }),
        ('Contenu', {
            'fields': ['title', 'content']
            }),
        ('Medias', {
            'fields': ['image']
        })
    ]
    def thumbnail_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="auto" />', obj.image.url)
        return '(Pas d\'image)'
    thumbnail_image.short_description = 'Aperçu de l\'image'

    def author_name(self, obj):
        if obj.author:
            return obj.author.first_name
        return '(Anonyme)'
    author_name.short_description = 'Auteur'

    def content_length(self, obj):
        if obj.content:
            return len(obj.content)
        return '(Pas de contenu)'
    content_length.short_description = 'Longueur du contenu'

class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'author_name', 'created_at']

    def author_name(self, obj):
        if obj.author:
            return obj.author
        return '(Anonyme)'
    author_name.short_description = 'Author'

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)

