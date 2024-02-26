from django.shortcuts import render

posts = [
    {
        'title' : 'Blog 1',
        'author' : 'awale1',
        'content' : 'First Blog Post!',
        'date' : 'Aug 13, 1998'
    }
]

def blog_home(request):
    return render(request, 'blog/blog_home.html', context={'posts' : posts})
