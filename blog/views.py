from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blog(request):
    blogs = Blog.objects.all()
    return render(request, "blog/all_blog.html", {'blogs': blogs})

def content(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blog_content.html', {'blog': blog})