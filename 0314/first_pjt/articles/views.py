from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
# view 함수들이 정의되는곳
# MTV 패턴의 V에 해당 

def index(request):
    return HttpResponse("<h1>작고 소중한 나의 첫 Django PJT</h1>")


def templates(request):
    return render(request,'index.html')
# 브라우저 화면을 만드는 과정 : 렌더링

def templates_first(request):
    return render(request,'firstapp/first.html')

def first(request):
    # 변수를 만들고
    name = '병국'
    job = '싸피싸피'
    menus = [0,1,2,3,4,5,6,7,8,9,10]
    title = 'mY NAME IS kUK BYUNG'
    #일반적으로 변수를 넘길 때 사용하는 방법
    context = {
        'name':name,
        'job':job,
        'menus':menus,
        'title' : title
    }
    # templates로 전달을 할 수 있다.
    # 마지막에 딕셔너리 형태로 전달
    # return render(request, 'firstapp/first.html', {'name':name, 'job':job})
    return render(request, 'firstapp/first.html', context)

def homework1_2(request):
    menus = [0,1,2,3]
    today = datetime.now()
    context = {
        'menus' : menus,
        'today' : today
    }
    return render(request, 'firstapp/homework1_2.html',context)