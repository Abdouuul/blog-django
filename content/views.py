from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models.article import Article
from .forms import CommentForm
from .models.comment import Comment

def article_list(request):
    articles = Article.objects.filter(is_published=True).order_by('-publication_date')

    return render(request, 'list.html', {'articles': articles})

def article_details(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                article=article,
                author = request.user if request.user.is_authenticated else None,
                content=form.cleaned_data['content']
            )
            messages.success(request, 'Votre commentaire a été ajouté avec succès.')
            comment.save()
            return redirect('article_details', article_id=article_id)
        
    comments = article.comments.all().order_by('-created_at')
    return render(request, 'article-details.html', {'article': article, 'comments': comments, 'form': form})


