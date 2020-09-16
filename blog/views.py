from django.shortcuts import render

# Create your views here.
from blog.models import Post


def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request,'blog/home.html', context)


def post_details(request,post_id):
    post_obj = Post.objects.get(id = post_id)
    print(post_id)
    context = {
        'post':post_obj
    }
    return render(request,'blog/post_details.html',context)