from django.urls import path
from .views import article_list, article_details
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', article_list, name='article_list'),
    path('article/<int:article_id>/', article_details, name='article_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)