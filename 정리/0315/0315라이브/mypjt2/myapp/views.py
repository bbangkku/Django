from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')


# urls.py 에 작성한 변수명이랑 동일하게 맞춰라
def detail(request, number):
    # URL 파라미터를 템플릿으로 전달
    context = {
        'number' : number,
    }
    return render(request, 'myapp/detail.html', context)
    
