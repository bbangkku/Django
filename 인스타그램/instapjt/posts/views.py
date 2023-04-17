from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# Create your views here.
def index(request):
    # posts = Post.obj
    return render(request, 'posts/index.html')
  

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    context ={'form' : form}
    return render(request, 'posts/create.html', context)
    
def read(request):
  pass