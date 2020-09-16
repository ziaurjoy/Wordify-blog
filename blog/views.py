from django.shortcuts import render

# Create your views here.
from blog.models import Post, Category


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

def filter_of_category(request,category_name):
    category_obj = Category.objects.get(name=category_name)
    print(category_obj)
    post_category = Post.objects.filter(category = category_obj)
    context = {'posts': post_category}
    return render(request,'blog/home.html',context)