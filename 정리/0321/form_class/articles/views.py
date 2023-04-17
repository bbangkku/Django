from django.shortcuts import render, redirect
from .models import Article
from .form import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)


def create(request):
    if request.method == 'POST':
        # 인코딩 되지 않은 이미지 파일은 request.FILES에 들어옴
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            # cleaned_data : form의 데이터를 파이썬 딕셔너리로 반환
            data = form.cleaned_data
            # 제목 : <사용자입력>
            article = Article(**data)
            article.save()
        return redirect('articles:detail', pk=article.pk)
    else:
        form = ArticleForm()
        context = {
            'form' : form
        }
        return render(request, 'articles/create.html',context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        # article.title = request.POST.get('title')
        # article.content = request.POST.get('content')
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid:
            form.save()
        # article.save()
            return redirect('articles:detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
        context = {'article': article,
                   'form': form,
                   }
        return render(request, 'articles/update.html', context)
