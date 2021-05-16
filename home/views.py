from django.shortcuts import render, get_object_or_404
from article.models import Article


# Create your views here.
def index(request):
    article = Article.objects.order_by('-created_date')
    context = {
        'article': article
    }
    return render(request, 'home/index.html', context)


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    return render(request, 'home/contact.html')


def detail(request, id):
    article = get_object_or_404('Article', id=id)
    context = {
        'article': article
    }
    return render(request, 'article/post', context)
