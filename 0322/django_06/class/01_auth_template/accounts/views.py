from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.

def login(request):
    if request.method == 'POST':
        print('>>>')
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            print('@@>>>')
            
            auth_login(request, form.get_user())
            return redirect('articles:index')
        # 로그인처리를 해줌
        # 1. 입력한 id, password 일치한다면 ?
        # 세션테이블 >, 쿠키에 정보 담고,,
    else:
        # 비어있는 로그인 페이지를 제공
        form = AuthenticationForm()
    context = {'form' : form }        
    return render(request,'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')