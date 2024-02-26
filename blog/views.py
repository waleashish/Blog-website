from django.shortcuts import render
from .models import Post

def blog_home(request):
    return render(request, 'blog/blog_home.html', context={'posts' : Post.objects.all()})
