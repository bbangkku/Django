from django.shortcuts import render, redirect
from .models import Article
# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    message = request.GET.get('message')
    context = {
        'message' : message
    }
    return render(request, 'articles/catch.html', context)

def articles(request):
    #전체 조회
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/articles.html', context)

def create(request):
    return render(request, 'articles/create.html')

# 실제로 데이터를 DB에 저장
def new(request):
    # 데이터 받아오기
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    # DB에 저장
    Article.objects.create(title=title, content=content)


    # 생성 후 전체 목록 리스트로 가야함
    # 현재는 아무것도 안보임
    # 새로고침하면 보임

    # return render(request, 'articles/articles.html')
    return redirect('articles:articles')





