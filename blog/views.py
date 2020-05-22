from django.shortcuts import render,get_object_or_404

from .models import Blog

def allblogs(request):
    blogs=Blog.objects
    return render(request,'allblogs.html',{'blog':blogs})

def detail(request,blog_id):
    dblog=get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'blog':dblog})