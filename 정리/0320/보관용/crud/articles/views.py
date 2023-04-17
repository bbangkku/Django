from django.shortcuts import render,redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request, 'articles/index.html',context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article':article}
    return render(request, 'articles/detail.html', context)
def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    # print(title,content)
    # # DB에 새로운 Article 저장
    # Article.objects.create(
    #     title=title,
    #     content=content)
    # 호출하고 저장하기전에 확인작업을 하는 과정
    article = Article(title=title, content=content)
    # ~~~~
    article.save()

    return redirect('articles:index')

