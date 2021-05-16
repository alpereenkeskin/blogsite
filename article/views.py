from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Article, commentModel
from .forms import Articleform
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def list(request):
    yazilar = Article.objects.all()
    context = {
        'yazilar': yazilar
    }
    return render(request, 'article/articles.html', context)


@login_required(login_url='user/login')
def dashboard(request):
    yazilar = Article.objects.filter(author=request.user)
    context = {
        'yazilar': yazilar
    }
    return render(request, 'article/dashboard.html', context)


def detail(request, id):
    article = get_object_or_404(Article, id=id)
    comments = article.comments.all()
    context = {
        'article': article,
        'comments': comments
    }
    return render(request, 'article/post.html', context)


def AddArticle(request):
    form = Articleform(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.add_message(request, messages.SUCCESS, 'Makaleniz başarı ile eklenmiştir.')
        return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'article/addarticle.html', context)


@login_required(login_url='user/login')
def update(request, id):
    article = get_object_or_404(Article, id=id)
    form = Articleform(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.add_message(request, messages.SUCCESS, 'Makale Başarı ile Güncellendi.')
        return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'article/update.html', context)


@login_required(login_url='user/login')
def delete(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    messages.add_message(request, messages.SUCCESS, 'Seçilen Makale Başarı ile silindi.')
    return redirect('dashboard')


def addcomment(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        comment_author = request.POST.get('comment_author')
        comment_content = request.POST.get('comment_content')

        newComment = commentModel(comment_author=comment_author, comment_context=comment_content)
        newComment.article = article
        newComment.save()
        messages.add_message(request, messages.SUCCESS, 'Yorum yapıldı.')
    return redirect('detail', str(id))


def sortBysofware(request):
    article = Article.objects.filter(catalog_id=1)
    context = {
        'yazilar': article
    }
    return render(request, 'article/articles.html', context)


def sortByengineer(request):
    article = Article.objects.filter(catalog_id=2)
    context = {
        'yazilar': article
    }
    if article:
        return render(request, 'article/articles.html', context)
    else:
        messages.add_message(request, messages.WARNING, 'İlgili konuda makale bulunmuyor.')
        return render(request, 'article/articles.html', context)
