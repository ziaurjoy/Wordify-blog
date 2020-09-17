from django.http import HttpResponse
from django.shortcuts import render
from blog.custom_context import my_context
# Create your views here.
from blog.models import Post, Category, Profile


def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request,'blog/home.html', context)


def post_details(request,post_id):
    try:
        post_obj = Post.objects.get(id = post_id)
        context = {
            'post': post_obj
        }
        return render(request,'blog/post_details.html',context)
    except Exception as err:
        print(err)
        return HttpResponse('404 Not Found')

def filter_of_category(request,category_name):
    category_obj = Category.objects.get(name=category_name)

    post_category = Post.objects.filter(category = category_obj)
    context = {'posts': post_category}
    return render(request,'blog/home.html',context)

def contact(request):
    return render(request,'blog/contact.html')

def about(request,profile_id):
    profile_obj = Profile.objects.get(id = profile_id)
    profile_post_filter = Post.objects.filter(author = profile_obj.user)
    context = {'profile': profile_obj, 'profile_filter': profile_post_filter}
    return render(request,'blog/about.html',context)