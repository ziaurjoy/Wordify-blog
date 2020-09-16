from blog.models import Category, Post


def my_context(request):
    category = Category.objects.all()
    latest_post = Post.objects.all().order_by('-create_on')[:3]
    return {'categoris': category,'latest_post': latest_post}