from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Article
from .forms import ArticleForm
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(['GET'])
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


def detail(request, pk):    
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)

@require_http_methods(['GET','POST'])
def create(request):
    if not request.user.is_authenticated:
        # reverse: 전달받은 Name에 매칭된 url을 문자열로 반환
        # print(reverse('accounts:login'))
        return redirect(reverse('accounts:login') + f'?next={request.path}')
        # return redirect(f'/accounts/login?next={request.path}')
        # return redirect('accounts:login')
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    next = request.GET.get('next')
    context = {
        'form': form,
        'next': next
        }
    return render(request, 'articles/create.html', context)

@require_http_methods(['POST'])
def delete(request, pk):
    if not request.user.is_authenticated:
        return redirect(reverse('accounts:login')+f'?next=/articles/{pk}')
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

@require_http_methods(['GET','POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {'form': form, 'article': article}
    return render(request, 'articles/update.html', context)
