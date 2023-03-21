from django.shortcuts import render, redirect
from .models import Article
from .form import ArticleModelForm

# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request,'articles/index.html',context)

def create(request):
    if request.method == "POST":    
        form = ArticleModelForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            article = Article(**data)
            article.save()
        return redirect('articles:detail', pk= article.pk)
    else:
        form = ArticleModelForm()
        context= {
            'form' : form
        }
        return render(request, 'articles/create.html',context)

def detail(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request,'articles/detail.html',context)