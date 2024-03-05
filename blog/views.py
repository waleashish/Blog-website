from django.shortcuts import render, redirect
from .models import Post

def blog_home(request):
    if (request.user.is_authenticated):
        return render(request, 'blog/blog_home.html', context={'posts' : Post.objects.all()})
    else:
        return redirect('login')
