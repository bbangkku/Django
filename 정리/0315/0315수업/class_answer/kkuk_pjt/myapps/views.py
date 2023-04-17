from django.shortcuts import render

def hello(request):
    return render(request, 'myapps/base.html')
# Create your views here.
