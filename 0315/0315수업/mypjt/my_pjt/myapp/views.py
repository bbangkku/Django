from django.shortcuts import render

# Create your views here.

def index(request):

    name = 'kkuk'
    info = {
        'name':'aiden',
        'age':21,

    }
    
    return render(request, 'myapp/index.html', {'info' : info})

