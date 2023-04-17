from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
##
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
# from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_POST,require_safe,require_http_methods
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import *
# Create your views here.
def login(request):
    next_url = request.GET.get('next')
    # print(request.GET)
    # print(next_url)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(next_url) if next_url else redirect('articles:index')
    else:
        form = AuthenticationForm()
    # next = request.GET.get('next')
    context = {
        'form': form,
        # 'next': next
        }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

# def signup(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request,user)
#             return redirect('articles:index')
#     else:
#         form = CustomUserCreationForm()
#     context = { 'form': form }
#     return render(request, 'accounts/signup.html', context)

# def singup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('articles:index')
#     else:
#         form = UserCreationForm()
#     context = {'form':form}
#     return render(request,'accounts/signup.html',context)



def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {'form':form}
    return render(request,'accounts/signup.html',context)


# @require_http_methods(['POST'])
# def delete(request):
#     user = request.user
#     user.delete()
#     auth_logout(request)
#     return redirect('articles:index')

@require_POST
def delete(request):
    if request.user.is_authenticated:
        
        request.user.delete()
        auth_logout(request)
    return redirect('articles:index')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = { 'form': form}
    return render(request, 'accounts/update.html', context)        

# def change_password(request):
#     if request == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#         return redirect('articles:index')
#     else:
#         form = PasswordChangeForm(request.user)
#     context = {'form':form}
#     return render(request, 'accounts/change_password.html',context)

@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # 로그인 유지하는거
            update_session_auth_hash(request,form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
