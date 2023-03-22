from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.


def login(request):
    if request.method == "POST":
            # 로그인 로직
            # 1. form 으로 데이터를 받아줌
            # 2. 유효성 검사
            # 3. 로그인
            # 4. index화면으로 리다이렉션
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            response = redirect("articles:index")
            # response.set_cookie('message','내가 만든 쿠키',5)
            # return redirect('articles:index')
            return response
    else:
        form = AuthenticationForm()
    context = { 'form':form }
    return render(request,'accounts/login.html',context)



def logout(request):
    auth_logout(request)
    return redirect('articles:index')
